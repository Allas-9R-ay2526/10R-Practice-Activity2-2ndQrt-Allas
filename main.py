# working with sets
from pyscript import document, display


def gobro(e):
    document.getElementById('div1').innerHTML = ''
    first_name = document.getElementById('fname').value
    last_name = document.getElementById('lname').value
    full_name= first_name + last_name


grade_seven = {'alice blue', 'barry allen'}
grade_eight = {'billy sparks', 'paige turner'}
grade_nine = {'anita williams', 'jackie kurr'}
grade_ten = {'sophia tan', 'daphne mariano'}

members = (grade_seven | grade_eight | grade_nine | grade_ten)
members.add(full_name)

display(grade_seven, target='div1')
display(grade_eight, target='div1')
display(grade_nine, target='div1')
display(grade_ten, target='div1')