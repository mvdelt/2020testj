
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
254
255
256
257
258
259
260
261
262
263
264
265
266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
284
285
286
287
288
289
290
291
292
293
294
295
296
297
298
299
300
301
302
303
304
305
306
307
308
309
310
311
312
313
314
315
316
317
318
using Confluent.Kafka;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Text;
using System.Threading.Tasks;
using System.Web;
namespace NaverBlog
{
    class Program
    {
        static void Main(string[] args)
        {
            var conf = new ProducerConfig
            {
                BootstrapServers = "mysterico.iptime.org:9091,mysterico.iptime.org:9092,mysterico.iptime.org:9093",
                Acks = Acks.Leader,
                Partitioner = Partitioner.ConsistentRandom,
                LingerMs = 3000,
                BatchNumMessages = 1,
                MessageSendMaxRetries = 2
            };
            var p = new ProducerBuilder<Null, string>(conf).Build();
            string KeyWord = "맥도날드";
            int indexPage = 1;
            while (true)
            {
                string indexUrl = "https://search.naver.com/search.naver?where=post&post_blogurl=naver.com";
                indexUrl += "&query=" + HttpUtility.UrlEncode(KeyWord);
                indexUrl += "&start=" + (indexPage - 1) * 10 + 1;
                indexPage++;
                string indexHtml = GetHtml(indexUrl);
                List<string> htmls = indexHtml.GetValues("//*[contains(@id, 'sp_blog')]", StringEx.XPathOption.OuterHtml);
                List<string> postUrls = new List<string>();
                foreach (var item in htmls)
                {
                    string makeUrl = item.Substring("<a href=\"", "\"");
                    postUrls.Add(makeUrl);
                }
                if (postUrls.Count <= 0) break;
                foreach (string postUrl in postUrls)
                {
                    string postHtml = GetPost(postUrl);
                    int totalPage = -1;
                    int comentPage = 1;
                    MockMessage mockMessage = new MockMessage();
                    mockMessage.brandId = "mcdonalds";
                    mockMessage.articleCode = postUrl;
                    mockMessage.channelKeyname = "naver-blog";
                    mockMessage.articleType = "p";
                    mockMessage.pageUrl = postUrl;
                    mockMessage.scrapContent = postHtml;
                    mockMessage.crawledAt = (long)(DateTime.Now - new DateTime(1970, 1, 1)).TotalMilliseconds;
                    string jsonString = mockMessage.ToJson();
                    lock (p)
                    {
                        p.Produce("topic-scrap-dev", new Message<Null, string>() { Value = jsonString });
                        p.Flush(TimeSpan.FromSeconds(10));
                    }
                    string blogNo = postHtml.Substring("blogNo = '", "'");
                    string logNo = postUrl.Substring("logNo=", "&");
                    if(string.IsNullOrWhiteSpace(logNo))
                    {
                        logNo = postUrl.Substring("logNo=");
                    }
                    do
                    {
                        string coomnetUrl = GetCommentUrl(blogNo, logNo, comentPage);
                        string commentHtml = GetComment(blogNo, logNo, postUrl, comentPage++);
                        string commentJsonText = commentHtml.Substring("jQuery(", ");");
                        CommentJson commentJson = commentJsonText.ToClass<CommentJson>();
                        if (commentJson?.result?.count == null) break;
                        if (totalPage == -1)
                        {
                            totalPage = commentJson.result.count.total / 50;
                            if ((commentJson.result.count.total % 50) > 0)
                            {
                                totalPage++;
                            }
                        }
                        foreach (CommentJson.Commentlist commentlist in commentJson.result.commentList)
                        {
                            MockMessage mockMessageComment = new MockMessage();
                            mockMessageComment.brandId = "mcdonalds";
                            mockMessageComment.parentPostCode = postUrl;
                            mockMessageComment.articleCode = commentlist.commentNo.ToString();
                            mockMessageComment.channelKeyname = "naver-blog";
                            mockMessageComment.articleType = "c";
                            mockMessageComment.pageUrl = coomnetUrl;
                            mockMessageComment.scrapContent = commentHtml;
                            mockMessageComment.crawledAt = (long)(DateTime.Now - new DateTime(1970, 1, 1)).TotalMilliseconds;
                            string jsonStringComment = mockMessageComment.ToJson();
                            lock (p)
                            {
                                p.Produce("topic-scrap-dev", new Message<Null, string>() { Value = jsonStringComment });
                                p.Flush(TimeSpan.FromSeconds(10));
                            }
                        }
                    } while (comentPage < totalPage);
                }
            }
        }
        private static string GetHtml(string url)
        {
            HttpWebRequest httpWebRequest = HttpWebRequest.Create(url) as HttpWebRequest;
            httpWebRequest.Method = "GET";
            httpWebRequest.UserAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36";
            httpWebRequest.Accept = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9";
            var httpWebResponse = httpWebRequest.GetResponse() as HttpWebResponse;
            string html = httpWebResponse.ReadToEnd(Encoding.UTF8);
            return html;
        }
        private static string GetPost(string url)
        {
            string html = GetHtml(url);
            string postUrl = html.Substring("window.location.href = \"", "\"");
            if (postUrl != null)
            {
                html = GetHtml(postUrl);
            }
            postUrl = html.Substring("/PostView.nhn?", "\"");
            postUrl = string.Format("https://blog.naver.com//PostView.nhn?{0}", postUrl);
            return GetHtml(postUrl);
        }
        private static string GetCommentUrl(string blogNo, string logNo, int page)
        {
            string url = "https://apis.naver.com/commentBox/cbox/web_naver_list_jsonp.json?ticket=blog&templateId=default&pool=cbox9&_callback=jQuery&lang=ko&country=&categoryId=&pageSize=50&indexSize=10&listType=OBJECT&pageType=default&initialize=true&userType=&useAltSort=true&replyPageSize=10&cleanbotGrade=2&showReply=true";
            url = url + "&objectId=" + blogNo + "_201_" + logNo;
            url = url + "&groupId=" + blogNo;
            url = url + "&page=" + page;
            return url;
        }
        private static string GetComment(string blogNo, string logNo, string referer, int page)
        {
            return GetComment(blogNo, logNo, referer, page, Encoding.UTF8);
        }
        private static string GetComment(string blogNo, string logNo, string referer, int page, Encoding encoding)
        {
            string url = "https://apis.naver.com/commentBox/cbox/web_naver_list_jsonp.json?ticket=blog&templateId=default&pool=cbox9&_callback=jQuery&lang=ko&country=&categoryId=&pageSize=50&indexSize=10&listType=OBJECT&pageType=default&initialize=true&userType=&useAltSort=true&replyPageSize=10&cleanbotGrade=2&showReply=true";
            url = url + "&objectId=" + blogNo + "_201_" + logNo;
            url = url + "&groupId=" + blogNo;
            url = url + "&page=" + page;
            HttpWebRequest httpWebRequest = HttpWebRequest.Create(url) as HttpWebRequest;
            httpWebRequest.Method = "GET";
            httpWebRequest.UserAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36";
            httpWebRequest.Accept = "*/*";
            httpWebRequest.Referer = referer;
            var httpWebResponse = httpWebRequest.GetResponse() as HttpWebResponse;
            string html = httpWebResponse.ReadToEnd(encoding);
            return html;
        }
    }
    public class MockMessage
    {
        public string brandId { get; set; }
        public string channelKeyname { get; set; }
        public string articleType { get; set; }
        public string articleCode { get; set; }
        public string parentPostCode { get; set; }
        public string pageUrl { get; set; }
        public string scrapContent { get; set; }
        public long crawledAt { get; set; }
    }
    public class CommentJson
    {
        public bool success { get; set; }
        public string code { get; set; }
        public string message { get; set; }
        public string lang { get; set; }
        public string country { get; set; }
        public Result result { get; set; }
        public DateTime date { get; set; }
        public class Result
        {
            public Commentlist[] commentList { get; set; }
            public Pagemodel pageModel { get; set; }
            public Exposureconfig exposureConfig { get; set; }
            public Count count { get; set; }
            public string listStatus { get; set; }
            public string sort { get; set; }
            public object[] bestList { get; set; }
        }
        public class Pagemodel
        {
            public int page { get; set; }
            public int pageSize { get; set; }
            public int indexSize { get; set; }
            public int startRow { get; set; }
            public int endRow { get; set; }
            public int totalRows { get; set; }
            public int startIndex { get; set; }
            public int totalPages { get; set; }
            public int firstPage { get; set; }
            public int prevPage { get; set; }
            public int nextPage { get; set; }
            public int lastPage { get; set; }
            public object current { get; set; }
            public object threshold { get; set; }
            public bool moveToLastPage { get; set; }
            public bool moveToComment { get; set; }
            public bool moveToLastPrev { get; set; }
        }
        public class Exposureconfig
        {
            public object reason { get; set; }
            public string status { get; set; }
        }
        public class Count
        {
            public int comment { get; set; }
            public int reply { get; set; }
            public int exposeCount { get; set; }
            public int delCommentByUser { get; set; }
            public int delCommentByMon { get; set; }
            public int blindCommentByUser { get; set; }
            public int blindReplyByUser { get; set; }
            public int total { get; set; }
        }
        public class Commentlist
        {
            public string ticket { get; set; }
            public string objectId { get; set; }
            public string categoryId { get; set; }
            public string templateId { get; set; }
            public long commentNo { get; set; }
            public long parentCommentNo { get; set; }
            public long replyLevel { get; set; }
            public long replyCount { get; set; }
            public long replyAllCount { get; set; }
            public object replyPreviewNo { get; set; }
            public object replyList { get; set; }
            public long imageCount { get; set; }
            public object imageList { get; set; }
            public object imagePathList { get; set; }
            public object imageWidthList { get; set; }
            public object imageHeightList { get; set; }
            public string commentType { get; set; }
            public object stickerId { get; set; }
            public object sticker { get; set; }
            public long sortValue { get; set; }
            public string contents { get; set; }
            public string userIdNo { get; set; }
            public object exposedUserIp { get; set; }
            public string lang { get; set; }
            public string country { get; set; }
            public string idType { get; set; }
            public string idProvider { get; set; }
            public string userName { get; set; }
            public string userProfileImage { get; set; }
            public string profileType { get; set; }
            public DateTime modTime { get; set; }
            public DateTime modTimeGmt { get; set; }
            public DateTime regTime { get; set; }
            public DateTime regTimeGmt { get; set; }
            public long sympathyCount { get; set; }
            public long antipathyCount { get; set; }
            public bool userBlind { get; set; }
            public bool hideReplyButton { get; set; }
            public long status { get; set; }
            public bool mine { get; set; }
            public bool best { get; set; }
            public object mentions { get; set; }
            public object toUser { get; set; }
            public long userStatus { get; set; }
            public object categoryImage { get; set; }
            public bool open { get; set; }
            public object levelCode { get; set; }
            public object grades { get; set; }
            public bool sympathy { get; set; }
            public bool antipathy { get; set; }
            public object snsList { get; set; }
            public object metaInfo { get; set; }
            public object extension { get; set; }
            public object audioInfoList { get; set; }
            public object translation { get; set; }
            public object report { get; set; }
            public bool middleBlindReport { get; set; }
            public object spamInfo { get; set; }
            public object userHomepageUrl { get; set; }
            public bool defamation { get; set; }
            public bool hiddenByCleanbot { get; set; }
            public object evalScore { get; set; }
            public bool visible { get; set; }
            public object serviceId { get; set; }
            public string idNo { get; set; }
            public bool manager { get; set; }
            public bool deleted { get; set; }
            public bool blindReport { get; set; }
            public bool anonymous { get; set; }
            public bool expose { get; set; }
            public bool secret { get; set; }
            public bool blind { get; set; }
            public object profileUserId { get; set; }
            public bool userBlocked { get; set; }
            public bool exposeByCountry { get; set; }
            public bool _virtual { get; set; }
            public bool containText { get; set; }
            public string maskedUserId { get; set; }
            public string maskedUserName { get; set; }
            public bool validateBanWords { get; set; }
        }
    }
}
