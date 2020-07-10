import types


class Metadata(types.SimpleNamespace):
    """
    A class that supports simple attribute setter/getter.
    It is intended for storing metadata of a dataset and make it accessible globally.

    Examples:

    .. code-block:: python

        # somewhere when you load the data:
        MetadataCatalog.get("mydataset").thing_classes = ["person", "dog"]

        # somewhere when you print statistics or visualize:
        classes = MetadataCatalog.get("mydataset").thing_classes
    """

    # the name of the dataset
    # set default to N/A so that `self.name` in the errors will not trigger getattr again
    # i. 바로윗줄의 말은, 현재시점에서의 내생각엔, 요바로아랫줄의 name 변수에 아무것도 할당된 값이 없으면, name을 불러오고자 할때 값이 없으니까 __getattr__를 실행할거자나. 그걸 막기 위함이다 라는 뜻인것같음. (참고로, 혹시까먹엇을까봐 적는데, __getattr__는 값을 찾아봐도 없을때 실행되는거고, __getattribute__은 값이 있든없든 걍 맨첨에 인터셉트해버리는놈인거 기억하지?ㅋ. getattr(x,'y')는 걍 x.y로 값 가져오는거랑 동일한거고.)
    name: str = "N/A_jjjhahajjj"

    _RENAMED = {
        "class_names": "thing_classes",
        "dataset_id_to_contiguous_id": "thing_dataset_id_to_contiguous_id",
        "stuff_class_names": "stuff_classes",
    }

    def __getattr__(self, key):
        if key in self._RENAMED:
            log_first_n(
                logging.WARNING,
                "Metadata '{}' was renamed to '{}'!".format(key, self._RENAMED[key]),
                n=10,
            )
            return getattr(self, self._RENAMED[key])

        raise AttributeError(
            "Attribute '{}' does not exist in the metadata of '{}'. Available keys are {}.".format(
                key, self.name, str(self.__dict__.keys())
            )
        )

    def __setattr__(self, key, val):
        if key in self._RENAMED:
            log_first_n(
                logging.WARNING,
                "Metadata '{}' was renamed to '{}'!".format(key, self._RENAMED[key]),
                n=10,
            )
            setattr(self, self._RENAMED[key], val)

        # Ensure that metadata of the same name stays consistent
        try:
            oldval = getattr(self, key)
            assert oldval == val, (
                "Attribute '{}' in the metadata of '{}' cannot be set "
                "to a different value!\n{} != {}".format(key, self.name, oldval, val)
            )
        except AttributeError:
            super().__setattr__(key, val)

    def as_dict(self):
        """
        Returns all the metadata as a dict.
        Note that modifications to the returned dict will not reflect on the Metadata object.
        """
        return copy.copy(self.__dict__)

    def set(self, **kwargs):
        """
        Set multiple metadata with kwargs.
        """
        for k, v in kwargs.items():
            setattr(self, k, v)
        return self

    def get(self, key, default=None):
        """
        Access an attribute and return its value if exists.
        Otherwise return default.
        """
        try:
            return getattr(self, key)
        except AttributeError:
            return default


print(Metadata.__dict__)
print('--------------------------------------------')
md1 = Metadata(name = 'name_JohnMan')
print(Metadata.__dict__)
print('--------------------------------------------')
print(md1.__dict__)
print('--------------------------------------------')
print(md1.name)
print('--------------------------------------------')
# print(md1.namehaha)