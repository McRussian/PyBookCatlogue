


class Author:
    def __init__(
            self,
            id: int = None,
            first_name: str = None,
            last_name: str = None,
            middle_name: str = None,
            alias: str = None,
    ):
        self.__id = id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__middle_name = middle_name
        self.__alias = alias

    @property
    def id(self) -> int:
        return self.__id

    @property
    def first_name(self) -> str:
        return self.__first_name

    @property
    def last_name(self) -> str:
        return self.__last_name

    @property
    def middle_name(self) -> str:
        return self.__middle_name

    @property
    def alias(self) -> str:
        return self.__alias

    def set_id(self, id: int):
        self.__id = id

    def set_first_name(self, first_name: str):
        self.__first_name = first_name

    def set_last_name(self, last_name: str):
        self.__last_name = last_name

    def set_middle_name(self, middle_name):
        self.__middle_name = middle_name

    def set_alias(self, alias: str):
        self.__alias = alias
