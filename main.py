from pyscript import display, document

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
            "Not eligible: student is not registered for Intrams. Ask your PE teacher regarding online registration.",
            target='output'
        )
    elif clearance != 'cleared':
        display(
            "Not eligible: medical clearance required. Please go to the clinic.",
            target='output'
        )
    elif grade_level < 7 or grade_level > 10:
        display(
            "Not eligible: only students from Grades 7 to 10 may join Intramurals.",
            target='output'
        )
    else:
        display(f"Congratulations! You are eligible to join Intramurals 🎉", target='output')

        if grade == '7':
            if section == 'ruby':
                document.getElementById("image").innerHTML = (
                    "<img src='yellow tigers.jpg' width='150' alt='Yellow Tigers'>"
                )
            elif section == 'emerald':
                document.getElementById("image").innerHTML = (
                    "<img src='green hornets.png' width='150' alt='Green Hornets'>"
                )
        
        if grade == '8':
            if section == 'ruby':
                document.getElementById("image").innerHTML = (
                    "<img src='blue bears.jpg' width='150' alt='Blue Bears'>"
                )
            elif section == 'emerald':
                document.getElementById("image").innerHTML = (
                    "<img src='red bulldogs'.png' width='150' alt='Red Bulldogs'>"
                )

        if grade == '9':
            if section == 'ruby':
                document.getElementById("image").innerHTML = (
                    "<img src='blue bears.jpg' width='150' alt='Blue Bears'>"
                )
            elif section == 'emerald':
                document.getElementById("image").innerHTML = (
                    "<img src='red bulldogs'.png' width='150' alt='Red Bulldogs'>"
                )

        if grade == '10':
            if section == 'ruby':
                document.getElementById("image").innerHTML = (
                    "<img src='yellow tigers.jpg' width='150' alt='Yellow Tigers'>"
                )
            elif section == 'emerald':
                document.getElementById("image").innerHTML = (
                    "<img src='green hornets.png' width='150' alt='Green Hornets'>"
                )
