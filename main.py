from __future__ import print_function
from mailmerge import MailMerge
from app import *


template="E:/teja.docx"

document=MailMerge(template)
print(document.get_merge_fields())
users = User.query.all()
for data in users:
    document.merge(
        name=data.name,
        state=data.state,
        nation=data.nation,
        date_of_test=data.date_of_test,
        age=data.age,
        postive_negitive=data.postive_negitive,
        present_residence=data.present_residence,
        phonenumber=data.phonenumber,
        address=data.address,
        collection_date=data.collection_date,
        village=data.village
    )
document.write('E:/test-output.docx')