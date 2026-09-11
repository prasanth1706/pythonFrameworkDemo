class User:
    def __init__(self, id: int, name: str, username: str, email: str, address: dict, phone: str, website: str, company: dict):
        self._id = id
        self._name = name
        self._username = username
        self._email = email
        self._address = address
        self._phone = phone
        self._website = website
        self._company = company

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name
    @property
    def username(self) -> str:
        return self._username

    @property
    def email(self) -> str:
        return self._email
    @property
    def address(self) -> dict:
        return self._address
    @property
    def phone(self) -> str:
        return self._phone
    @property
    def website(self) -> str:
        return self._website
    @property
    def company(self) -> dict:
        return self._company
    