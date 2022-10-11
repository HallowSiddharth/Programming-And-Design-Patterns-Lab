class Library:
    def __init__(self):
        self.data={"Book":{},"CD":[],"Magazine":[],"Audio Book":[]}
        self.size=0

    def add(self,type):
        upc=input("Enter UPC: ")
        if type=="Book":
            book=input("Enter the name of the book : ")
            author=input("Enter name of author : ")
            isbn=int(input("Enter the ISBN : "))
            dds=int(input("Enter the DDS : "))
            if dds in self.data["Book"][dds]:
                self.data["Book"][dds].append([isbn,upc,book,author,dds])
                self.data["Book"][dds].sort()
            else:
                self.data["Book"][dds]=[[isbn,upc,book,author,dds]]
        elif type=="Magazine":
            name=input("Enter the name of the magazine : ")
            volume=int(input("Enter the volume number : "))
            isno=int(input("Enter the issue no. :"))
            self.data["Magazine"].append([upc,name,volume,isno])
        elif type=="CD":
            author=input("Enter the name of the CD : ")
            self.data["CD"].append()
            
    