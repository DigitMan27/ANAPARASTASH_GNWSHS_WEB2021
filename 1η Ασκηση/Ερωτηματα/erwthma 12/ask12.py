from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from lxml import etree

from ask12_ui import Ui_XML_Win

class xml_handler(QtWidgets.QMainWindow):
	def __init__(self):
		super(xml_handler,self).__init__()
		self.ui = Ui_XML_Win()
		self.ui.setupUi(self)
		self.error_dialog = QtWidgets.QMessageBox()
		self.rows = 0 # αριθμος γραμμών του πινακα

		# buttons
		self.ui.xml_input.clicked.connect(self.__addxml)
		self.ui.xsd_input.clicked.connect(self.__addxsd)
		self.ui.submit.clicked.connect(self.__show2table)
		self.ui.add_to_xml.clicked.connect(self.__add2xml)

		#Table
		self.model = QtGui.QStandardItemModel()
		self.model.setHorizontalHeaderLabels(['Lesson','Professor','Day'])
		self.ui.Data.setModel(self.model)
		self.ui.Data.setColumnWidth(0,170)
		self.ui.Data.setColumnWidth(1,110)

		self.path_xml = None # μονοπάτι του xml αρχείου
		self.path_xsd = None # μονοπάτι του xsd αρχείου

	def __addxml(self):
		options = QtWidgets.QFileDialog.Options()
		options |= QtWidgets.QFileDialog.DontUseNativeDialog
		fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self,"Open", "","XML File (*.xml)", options=options)
		self.path_xml = fileName


	def __addxsd(self):
		options = QtWidgets.QFileDialog.Options()
		options |= QtWidgets.QFileDialog.DontUseNativeDialog
		fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self,"Open", "","XSD File (*.xsd)", options=options)
		self.path_xsd = fileName

	def __show2table(self):
		# καθαρισμος πινακα απο προηγούμενες εγγραφες
		self.rows = 0
		self.model.clear()
		self.model.setHorizontalHeaderLabels(['Lesson','Professor','Day'])
		self.ui.Data.setColumnWidth(0,170)
		self.ui.Data.setColumnWidth(1,110)
		xml_f = None
		xsd_f = None
		tmp_prof = "" # προσωρινη μεταβλητη για τον καθηγητη
		tmp_title = "" # προσωρινη μεταβλητη για τον τιτλο
		titles = [] # λιστα που περιεχει ολα τα μαθήματα(τιτλους)
		profs = [] # λιστα που περιεχει ολους τους καθηγητες
		days = [] # # λιστα που περιεχει ολες τις μερες που γινονται τα μαθήματα
		flag = False # σημαία για το αν υπάρχει το στοιχείο Professor στο καθε Lesson αν οχι τοτε μπαινει κενο
		day_count = 0 # αριθμος μερων που γινεται το μαθημα
		days_filter = []
		text = str(self.ui.filter.currentText())
		if(text=="All Days"):
			days_filter = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
		else:
			days_filter.append(text)
		if(self.path_xsd and self.path_xml):
			xsd_f = etree.parse(self.path_xsd)
			xsd = etree.XMLSchema(xsd_f)
			xml_f = etree.parse(self.path_xml)
			if(xsd.validate(xml_f)): # validation με το xsd αρχείο
				self.error_dialog.about(self,'Result','Το XML Αρχείο είναι εγκυρο!')
				root = xml_f.getroot()
				for child in root.getchildren():
					for elem in child.getchildren():
						elem.tag = etree.QName(elem).localname # παιρνω το τοπικό ονομα και αποφευγω ετσι την εμφάνιση του namespace
						if elem.tag=="Title":
							tmp_title = elem.text
						elif elem.tag=="Professor":
							tmp_prof = elem.text
							flag = True
							for p in range(0,day_count):
								profs.append(tmp_prof)
						for day in elem.getchildren():
							day.tag = etree.QName(day).localname
							if day.tag=="Day" and day.text in days_filter: # Αν βρει το στοιχείο Day και το text της ειναι ιδιο με την τιμη του φιλτρου
								day_count+=1
								days.append(day.text)
								titles.append(tmp_title)
					if(flag==False): # αν δεν υπαρχει Professor tag
						for p in range(0,day_count):
							profs.append(" ")
					day_count=0
					tmp_prof = ""
					flag = False
				for title,prof,day in zip(titles,profs,days): # απεικονιση στοιχείων στον πινακα
					qtitle = QtGui.QStandardItem(title)
					qprof = QtGui.QStandardItem(prof)
					qday = QtGui.QStandardItem(day)
					self.model.setItem(self.rows,0,qtitle)
					self.model.setItem(self.rows,1,qprof)
					self.model.setItem(self.rows,2,qday)
					self.rows+=1

			else:
				self.error_dialog.about(self,'Error','Το XML Αρχείο δεν είναι εγκυρο!')
				return

		else:
			self.error_dialog.about(self,'Error','Το αρχείο XML/XSD λείπει!')
			return

	def __add2xml(self):
		if(not self.path_xml):
			self.error_dialog.about(self,'Error','Το αρχείο XML λείπει!')
			return

		parser = etree.XMLParser(remove_blank_text=True)
		xml_f = etree.parse(self.path_xml,parser)
		root = xml_f.getroot() # παιρνω την ριζα 
		lesson = self.ui.Lesson_val.text() # τιμη του πεδίου Title
		prof = self.ui.Professor_val.text() # τιμη του πεδίου Professor
		day = self.ui.Day_val.text() # τιμη του πεδίου Day
		if(not lesson or not day):
			self.error_dialog.about(self,'Error','Κάποιο απο τα πεδία(Title/Day) δεν έχει σωστή τιμή!')
			return
		if day not in ["Monday","Tuesday","Wednesday","Thursday","Friday"]:
			self.error_dialog.about(self,'Error','Το πεδίο Day δεν περιέχει μια μέρα της εβδομάδας!')
			return
		lesson_elem = etree.SubElement(root,'Lesson')
		title_elem = etree.SubElement(lesson_elem,'Title')
		title_elem.text = lesson
		lect_elem = etree.SubElement(lesson_elem,'Lecture')
		day_elem = etree.SubElement(lect_elem,'Day')
		time_elem = etree.SubElement(lect_elem,'Time')
		day_elem.text = day
		time_elem.text = "10:30-12:30" # μια τυχαία ώρα
		if(prof): # αν υπάρχει τιμη το πεδίο του Professor
			prof_elem = etree.SubElement(lesson_elem,'Professor')
			prof_elem.text = prof
		f = open(self.path_xml,'w')
		f.write(etree.tostring(root,pretty_print=True).decode())
		f.close()




if __name__=="__main__":
	app = QtWidgets.QApplication(sys.argv)
	window = xml_handler()
	window.show()
	sys.exit(app.exec_())