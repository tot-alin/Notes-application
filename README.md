# Notes Application

Notes application is a versatile tool that allows users to quickly edit and organize textual information, such as ideas, tasks, events, etc., related to a specific calendar date. The data is saved in a database that can be accessed with a username and password.

demo 
* username:inventii  
* password:1234
<br />
<br />

## Technologies used
* Python -Python is a dynamic, high-level, object-oriented programming language developed by Guido van Rossum in 1989
* SQLite (sqlite3) - sqlite3 is an API for SQLite, it realizes a database on the physical memory medium of the computer
* Google Text-to-Speech (gtts) - Google Text-to-Speech API, converts input text to audio
* PyFPDF (fpdf) - PyFPDF is a library for generating PDF documents in the Python programming environment, ported from PHP
* playsound (playsound3) - Audio playback module, used on multiple platforms with a single function and no dependencies
* Python OS (os) - The module provides facilities for interaction between the programming environment and the operating system.
* Python DateTime (datetime) - The module provides classes for manipulating date, time and time intervals, suitable for scenarios that require complex calculations and formatting
* Python Time (time) - module that provides various methods to work with time-related operations in particular for measuring execution time, pausing execution and retrieving the current time.
* Tk (tkinter) - is a standard Python GUI (Graphical User Interface) library that provides a set of tools and widgets to create desktop applications with graphical user interfaces.
<br />
<br />

## Application structure
The accompanying diagram illustrates the hierarchical architecture of classes and their functional association.

<p align="center">
<img width="357" height="256" alt="image" src="https://github.com/user-attachments/assets/559238d6-2278-45a1-b2a4-02c567b1fe16" />
</p> 

## Application features

<p align="center">
<br />Initial window & WinStart class methods
  
<br /><img width="331" height="338" alt="image" src="https://github.com/user-attachments/assets/cba00906-7296-403a-8e8e-bc26c7d203b1" /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <img width="530" height="318" alt="image" src="https://github.com/user-attachments/assets/aa65cd3c-6149-4b65-99cd-bb6d6fa2c9c0" />
</p> 
<br />

<p align="center">
<br />Sing in window & Sing In class methods
  
<br /><img width="478" height="171" alt="image" src="https://github.com/user-attachments/assets/49ef7a07-dd78-4672-9558-5fea86e7442d" /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <img width="468" height="243" alt="image" src="https://github.com/user-attachments/assets/1c623054-ab95-4623-8c8f-3d49edf303fc" />
</p> 
<br />

<p align="center">
<br />Window create account & Methods of class create account
  
<br /><img width="484" height="208" alt="image" src="https://github.com/user-attachments/assets/d5787344-66e4-424c-a6da-b3078705be7b" /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <img width="458" height="219" alt="image" src="https://github.com/user-attachments/assets/051982a8-7aa2-45c6-8fe4-19de0aa31eca" />
</p> 
<br />

<p align="center">
<br />Notes App window & NoteApp class methods
  
<br /><img width="1155" height="711" alt="image" src="https://github.com/user-attachments/assets/18139a30-d4f7-42a6-ac43-78ab65105143" /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <img width="414" height="614" alt="image" src="https://github.com/user-attachments/assets/58cb08a5-4839-4961-a7cb-91ee0b363865" />
</p> 
<br />

<p align="center">
<br />Illustration of scroll bars & Code that scrolls the Note App window
  
<br /><img width="710" height="517" alt="image" src="https://github.com/user-attachments/assets/b1515d87-3a0d-47a0-8d33-9fa3d6000044" /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <img width="904" height="276" alt="image" src="https://github.com/user-attachments/assets/a0972366-fb5a-4bbf-8249-e88fae72f02d" />
</p> 
<br />

<p align="center">
<br />Selection window & The "bind" method for double-click selection & The window reordering method
  
<br /><img width="499" height="240" alt="image" src="https://github.com/user-attachments/assets/6797d240-bc09-4c3d-a235-998c62405f73" /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <img width="912" height="135" alt="image" src="https://github.com/user-attachments/assets/7f2feb50-db5b-4b58-b436-47b65c7e1444" />  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <img width="933" height="297" alt="image" src="https://github.com/user-attachments/assets/c7d824f3-3c12-4dd0-b992-2eb4914dafc9" />
</p> 
<br />
<br />

## The window reordering method
* test_db - test if the database exists
* open_sql - open and connect to the database
* close_sql - close the cursor and the connection to the database
* insert_user - write user password, and create new table
* ver_user_password - check user and password in the intended table (users)
* save_data - save notes to table named after user name
* in_sort - pre-sort table information to refresh_list_box sorted in the form requested by list_box
* refresh_list_box - send list_box the requested data
* get_data_db - search database for user information and record parameters 
* del_record - delete a record
* up_record - modify a record

<p align="center">
<br /><img width="651" height="574" alt="image" src="https://github.com/user-attachments/assets/8f1cbe39-1c90-47fb-876e-dad6f5a4c383" />
</p> 
<br />
<br />

## ExportPdfDoc and Audio class methods
class ExportPdfDoc
* The export_to_pdf method is called from the NoteApp class with the parameters title and content text. This method generates a PDF document according to a given template.

class Audio
* The create_sound method prepends the text and language setting using the gTTs API and passes it to a server which converts it to an audio file
* The play method prepends the file created by the create_sound method and plays it, after which it will delete the audio file

<p align="center">
<br /><img width="432" height="291" alt="image" src="https://github.com/user-attachments/assets/b0ed7fb7-7868-4bd0-849f-36264542ef52" />
</p> 
<br />
<br />

## Bibliography:

https://ro.wikipedia.org/wiki/Python

https://pyfpdf.readthedocs.io/en/latest/

https://github.com/pndurette/gTTS

https://pypi.org/project/playsound3/

https://docs.python.org/3/library/sqlite3.html

https://docs.python.org/3/library/datetime.html

https://levelup.gitconnected.com/time-module-vs-datetime-module-in-python-f4a5e818350a

https://www.geeksforgeeks.org/introduction-to-tkinter/
