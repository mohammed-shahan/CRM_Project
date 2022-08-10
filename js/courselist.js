var courses = [
    {
        code: 'CRM010',
        name: 'Physics',
        description: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptatum officiis maiores iure odit nisi corporis corrupti, similique ea provident nam dolorum ex voluptatem amet, sint quidem? Cum nulla quo ab.',
        trainer: 'Abhilash Nelson',
        duration: 20, // days
        startDate: '26/05/2022',
        amount: 80000,
    },
    {
        code: 'CRM011',
        name: '',
        description: '',
        trainer: '',
        duration: 0, // days
        startDate: '',
        amount: 0,
    },
    {
        code: '',
        name: '',
        description: '',
        trainer: '',
        duration: 0, // days
        startDate: '',
        amount: 0,
    },
    {
        code: '',
        name: '',
        description: '',
        trainer: '',
        duration: 0, // days
        startDate: '',
        amount: 0,
    },
    {
        code: '',
        name: '',
        description: '',
        trainer: '',
        duration: 0, // days
        startDate: '',
        amount: 0,
    },
    {
        code: '',
        name: '',
        description: '',
        trainer: '',
        duration: 0, // days
        startDate: '',
        amount: 0,
    },
    {
        code: '',
        name: '',
        description: '',
        trainer: '',
        duration: 0, // days
        startDate: '',
        amount: 0,
    },
]

function listCourses() {
    const table = document.getElementById('courselist')
    table.innerHTML = ''
    
    courses.forEach((course, index) => {
        var row = document.createElement('tr')
        table.appendChild(row)
        var code = row.insertCell(0);
        var name = row.insertCell(1);
        var trainer = row.insertCell(2);
        var date = row.insertCell(3);
    
        row.id = index;
        code.innerHTML = course.code;
        name.innerHTML = course.name;
        trainer.innerHTML = course.trainer;
        date.innerHTML = course.startDate;
    
        row.addEventListener('click', viewCourse)
    });
}


function viewCourse(event) {
    courseDetail = document.getElementById('course-detail')
    courseDetail.innerHTML = ''

    var courseDet = document.createElement('div')
    courseDet.className = 'col s4'
    
    var courseDesc = document.createElement('div')
    courseDesc.className = 'col s8'
    var dect = document.createElement('h4')
    dect.innerHTML = 'Description'
    courseDesc.appendChild(dect)
    courseDesc.innerHTML += courses[event.target.parentElement.id].description;

    courseDetail.appendChild(courseDet)
    courseDetail.appendChild(courseDesc)
    
    var heading = document.createElement('h3')
    heading.innerHTML = courses[event.target.parentElement.id].name;
    courseDet.appendChild(heading)

    var trainer = document.createElement('div')
    trainer.innerHTML = 'Trainer: ' + courses[event.target.parentElement.id].trainer
    courseDet.appendChild(trainer)

    var duration = document.createElement('div')
    duration.innerHTML = 'Duration: ' + courses[event.target.parentElement.id].duration
    courseDet.appendChild(duration)

    var date = document.createElement('div')
    date.innerHTML = 'Date: ' + courses[event.target.parentElement.id].startDate
    courseDet.appendChild(date)

    var amount = document.createElement('div')
    amount.innerHTML = 'Amount: ' + courses[event.target.parentElement.id].amount
    courseDet.appendChild(amount)

    courseDetail.style.display = 'block';
}

listCourses()