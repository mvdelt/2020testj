var fs = require('fs')

function mkdirOnlyNotExistj(path, mask, cb) {
    if (typeof mask == 'function') { // allow the `mask` parameter to be optional
        cb = mask;
        mask = 0777;
    }
    fs.mkdir(path, mask, function(err) {
        if (err) {
            if (err.code == 'EEXIST') {
                console.log('j) dir already exist. Ignoring EEXIST error...')
                cb(null); // ignore the error if the folder already exists
            }
            else cb(err); // something else went wrong
        } else cb(null); // successfully created folder
    })
}

// i. 파이썬의 if __name__ = '__main__' 같은 역할.
if (require.main === module){
    // And we can use it like this:
    mkdirOnlyNotExistj(__dirname + '/makeDirTestj', 0744, function(err) {
        if (err){
            // handle folder creation error
            console.error(err)
        } 
        else{ // we're all good
            console.log('j) mkdir successfully finished.')
        }
    })
}

module.exports = mkdirOnlyNotExistj
// module.exports = {mkdirOnlyNotExistj, some_another_fct1, some_another_fct2, ...} // i. 만약 익스포트하고싶은게 여러개면 이렇게 묶어서 하면 됨.