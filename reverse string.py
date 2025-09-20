class Reverser:
    def reverse(self,text):
        return" ".join(word[::-1] for word in text.split())
r=Reverser()
print(r.reverse("Hello world this is Python"))