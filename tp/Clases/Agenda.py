class Contact:
    def __init__(self,name,mail,tel):
        self.name=name
        self.mail=mail
        self.tel=tel
        
class Agenda:
    def __init__(self):
        self.contact_list=[]
    
    def add_contact_to_list(self,name,mail,tel):
        new_contact=Contact(name,mail,tel)
        self.contact_list.append(new_contact)
        print("Se agrego el contacto")
        
    def list_contact(self):
        if  not self.contact_list:
            print("La lista de contactos esta vacia ")
        else:
            self.contact_list = sorted(self.contact_list, key=lambda contact: contact.name)
            print("Lista de contactos: ")
            i=1
            for contact in self.contact_list:
                print(f"{i}) {contact.name} su mail es  {contact.mail}  tel:{contact.tel}")
                i+=1
                
    def search_contact(self,name):
        for contact in self.contact_list:
            if name==contact.name:
                print(f"{contact.name} su mail es  {contact.mail}  tel:{contact.tel}")
            else:
                print(f"contacto inexistente")
                
    def edit_contact(self,name,tel,mail):
        for contact in self.contact_list:
            if name==contact.name:
                contact.tel=tel
                contact.mail=mail
                print(f"Los datos se actualizaron a : Nombre :{contact.name} mail : {contact.mail}  tel:{contact.tel}")
            else:
                print(f"contacto inexistente")