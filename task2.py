from typing import List

class SocialNetwork:

    def __init__(self, name: str, users: int):
        """
        Initialize a social network.

        """
        self.name = name
        self.users = users

    def __str__(self) -> str:
        """
        Return a string representation of the social network.
        """
        return f"{self.name} - Users: {self.users}"

    def __repr__(self) -> str:
        """
        Return a string representation of the social network object.

        """
        return f"{self.__class__.__name__}(name={self.name!r}, users={self.users!r})"


class VK(SocialNetwork):
 

    def __init__(self, name: str, users: int, groups: List[str]):
        """
        Initialize a VK social network.
        """
        super().__init__(name, users)
        self.groups = groups

    def get_most_popular_groups(self) -> List[str]:
        """
        Get the most popular groups in VK.

        """
      
        pass

    def __str__(self) -> str:
        """
        Return a string representation of the VK social network.

        """
        return f"VK - Users: {self.users}, Groups: {len(self.groups)}"

   
    def __repr__(self) -> str:
        """
        Return a string representation of the VK social network object.
        """

        return f"{self.__class__.__name__}(name={self.name!r}, users={self.users!r}, groups={self.groups!r})"


class Facebook(SocialNetwork):

    def __init__(self, name: str, users: int, pages_liked: int):
        """
        Initialize a Facebook social network.

        """
        super().__init__(name, users)
        self.pages_liked = pages_liked

    def get_top_liked_pages(self) -> List[str]:
        """
        Get the top liked pages on Facebook.

        """
        
        pass

    def __str__(self) -> str:
        """
        Return a string representation of the Facebook social network.

        """
        return f"Facebook - Users: {self.users}, Pages Liked: {self.pages_liked}"

  
    def __repr__(self) -> str:
        """
        Return a string representation of the Facebook social network object.

        """
        return f"{self.__class__.__name__}(name={self.name!r}, users={self.users!r}, pages_liked={self.pages_liked!r})"


if __name__ == "__main__":
    vk = VK(name="VK", users=10000000, groups=["Music", "Movies", "Games"])
    print(vk)
    print(repr(vk))

    facebook = Facebook(name="Facebook", users=250000000, pages_liked=500000000)
    print(facebook)
    print(repr(facebook))
