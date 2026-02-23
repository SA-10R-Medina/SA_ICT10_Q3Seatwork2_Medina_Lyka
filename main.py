from pyscript import display
from js import document

def intrams_checker(e):
    document.getElementById('output').innerHTML = ''
    document.getElementById('image').innerHTML = ''

    registration_input = document.querySelector('input[name="registration"]:checked')
    clearance_input = document.querySelector('input[name="clearance"]:checked')

    if registration_input is None or clearance_input is None:
        display("Please answer all the questions.", target="output")
        return

    registration = registration_input.value
    clearance = clearance_input.value
    grade_level = int(document.getElementById('level').value)
    section = document.getElementById('section').value

    if registration != 'registered':
        display(
            "u not registered🤨",
            target='output'
        )
    elif clearance != 'cleared':
        display(
            "u fragile😛",
            target='output'
        )
    else:
        display(f"Enjoy Intrams!", target='output')

        if grade_level == 7:
            if section == 'ruby':
                document.getElementById("image").innerHTML = (
                    "<img src='yellow tigers.jpg' width='150' alt='Yellow Tigers'>"
                )
            elif section == 'emerald':
                document.getElementById("image").innerHTML = (
                    "<img src='green hornets.png' width='150' alt='Green Hornets'>"
                )
        
        if grade_level == 8:
            if section == 'ruby':
                document.getElementById("image").innerHTML = (
                    "<img src='blue bears.jpg' width='150' alt='Blue Bears'>"
                )
            elif section == 'emerald':
                # ↓ Corrected malformed src attribute (removed stray period and extra quote)
                document.getElementById("image").innerHTML = (
                    "<img src='red bulldogs.png' width='150' alt='Red Bulldogs'>"
                )

        if grade_level == 9:
            if section == 'ruby':
                document.getElementById("image").innerHTML = (
                    "<img src='blue bears.jpg' width='150' alt='Blue Bears'>"
                )
            elif section == 'emerald':
                # ↓ Same src correction as above
                document.getElementById("image").innerHTML = (
                    "<img src='red bulldogs.png' width='150' alt='Red Bulldogs'>"
                )

        if grade_level == 10:
            if section == 'ruby':
                document.getElementById("image").innerHTML = (
                    "<img src='yellow tigers.jpg' width='150' alt='Yellow Tigers'>"
                )
            elif section == 'emerald':
                document.getElementById("image").innerHTML = (
                    "<img src='green hornets.png' width='150' alt='Green Hornets'>"
                )
