class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "null"

        encoded = ""

        for word in strs:
            encoded += word + ":;"
        return encoded[:-2]

    def decode(self, s: str) -> List[str]:
        if s == "null":
            return []

        return s.split(":;")