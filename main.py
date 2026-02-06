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

        if section == 'emerald':
            document.getElementById("image").innerHTML = "<img src='emerald.png' width='150'>"
        elif section == 'ruby':
            document.getElementById("image").innerHTML = "<img src='ruby.png' width='150'>"
        elif section == 'sapphire':
            document.getElementById("image").innerHTML = "<img src='sapphire.png' width='150'>"
        else:
            document.getElementById("image").innerHTML = "<img src='topaz.png' width='150'>"
