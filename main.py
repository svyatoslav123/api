from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
import requests
app = QApplication([])

window = QWidget()
window.resize(200, 100)

otrym = QPushButton("Отримати результат")
valute = QLineEdit("")
data = QLineEdit("")
rezult = QLineEdit("")

main_line = QVBoxLayout()

h1 = QHBoxLayout()
h2 = QHBoxLayout()
h3 = QHBoxLayout()
h4 = QHBoxLayout()


h1.addWidget(valute)
h2.addWidget(data)
h3.addWidget(rezult)
h4.addWidget(otrym)


main_line.addLayout(h1)
main_line.addLayout(h2)
main_line.addLayout(h3)
main_line.addLayout(h4)

def dd():
    valcode = valute.text()
    date = data.text()
    url1 = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={valcode}&date={date}&json"
    r = requests.get(url1)
    if r.status_code == 200:
        res = r.json()
        rezult.setText(str(res[0]["rate"]))








otrym.clicked.connect(dd)
window.setLayout(main_line)
window.show()
app.exec()