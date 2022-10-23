import flet
from flet import ( FloatingActionButton, Page, TextField, icons,Text,AppBar,Icon,
IconButton,Page,colors,ListView,Dropdown,dropdown,Container,Row,alignment,border_radius
,AlertDialog,Checkbox,Column,Row)


def main (page:Page):

    #Variable
    show_dlg = page.dialog = AlertDialog(title=Text("No Todo List"))
    todolist = ListView()
    read_txt = Column()
    read_realtxt = Column()
    new_task=TextField(hint_text='Enter Your To Do List',autofocus=True,width=800)



    #delete 
    # def delete_txt():
    def display_task(task_name):
        Checkbox(value=False, label=task_name,)



    #Show content
    def show_text(content_):  
        return Row([Container(
            content=Text(value=content_,size=25,color=colors.BROWN),
            width=500,
            height=450,
            bgcolor=colors.PINK_50,
            alignment=alignment.center,
            border_radius=border_radius.all(5)        
        )],alignment='center')


    def write_txt(write):
        with open('test_file.txt','w+') as text:
            read_realtxt = Column()

            for i in write:
                text.write(f'{i}\n')
            
        with open('test_file.txt','r') as read_text:
            for j in read_text:            
                j = j.replace("\n", "")
                if j !='':
                    read_realtxt.controls.append(Text(f"{j}"))

            
            page.clean()
            page.add(display,read_realtxt)
            page.update()

            print(write)
   

    #Write to filet text 
    def keep_txt(write):
        with open('test_file.txt','a+') as text:
            text.write(f'{write}\n')
            print(write)


    #Read file text
    def read_file():
        with open('test_file.txt','r') as file_read:
            for i in file_read:            
                i = i.replace("\n", "")
                if i !='':
                    read_txt.controls.append(Text(f"{i}"))



    #Realtime
    def real_text(text):
        read_txt.controls.append(Text(f"{text}"))

    
   
    


    #Click Button
    def addclick(button):
        #Chaeck empty
        if new_task.value == "":
            print("todo is empty")
            page.dialog = show_dlg
            show_dlg.open = True
        else:
            keep_txt(new_task.value)
            real_text(new_task.value)
            new_task.value = str()       
        page.update()

    def delclick(button):
        list_txt = list()
        with open('test_file.txt','r') as file_read:
            for i in file_read:
                            
                i = i.replace("\n", "")
                if new_task.value == i:
                    print(i)
                else:
                    print(i)
                    list_txt.append(i)
                   
            print(list_txt)
            write_txt(list_txt)
            new_task.value = str()


            
        


    #Dropdown Changed
    read_file()
    a=read_txt
    def dropdown_changed(e):
        #Todolist
        count2 =0
        for x in d:
            if knowledge.value==(f'{count2+1}){x["หัวข้อ"]}'):
                page.clean()
                page.add(display)
                page.add(show_text(x["บทความ"]))
            count2 +=1


    #Show Dropdown list Todolist
    knowledge=Dropdown(on_change = dropdown_changed,
        label="List & Poem",
        hint_text="",
        width=430,
        options=[],
        autofocus=True,
        )



    #Show list Dropdown Content
    with open("working.txt","r",encoding="utf-8") as read_knowledge:
        a1 = read_knowledge.readlines()
        d = []
        know_dict = {}
        counts=0
        for i in a1:
            i=i.replace("\n","")
            Subject,Content = i.split(", ")
            know_dict = {"หัวข้อ":(Subject),"บทความ":(Content)}
            d.append(know_dict)
            counts+=1
            knowledge.options.append(dropdown.Option(f'{counts}){Subject}'))
    display = Row([new_task,FloatingActionButton(icon=icons.ADD,on_click=addclick),FloatingActionButton(icon=icons.ADD,on_click=delclick),knowledge,])
   

   
    #Show page
    page.add(display,a)
    

    #Show Appbar
    page.appbar = AppBar(
        leading=Icon(icons.TIMELAPSE_ROUNDED),
        leading_width=30,
        title=Text('TO DO LIST'),
        center_title= False,
        elevation=1,
        bgcolor=colors.PINK_100,
       )


    

   
    page.update()
#Run app
flet.app(target=main)