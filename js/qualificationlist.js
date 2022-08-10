var qualifications = [
    {
        code: 'Q001',
        name: 'B.Tech',
    },
    {
        code: 'Q002',
        name: 'M.Tech',
    },
]

const table = document.getElementById('qualifications')

var count = 1;
qualifications.forEach((q, index) => {
    var row = table.insertRow(count++);
    var code = row.insertCell(0);
    var name = row.insertCell(1);

    row.id = index;
    code.innerHTML = q.code;
    name.innerHTML = q.name;

    row.addEventListener('click', viewQualification)
});

function viewQualification(event) {
    qualDetail = document.getElementById('qualification-detail')
    qualDetail.innerHTML = ''

    var code = document.createElement('div')
    code.innerHTML = 'Code: ' + qualifications[event.target.parentElement.id].code
    qualDetail.appendChild(code)

    var name = document.createElement('div')
    name.innerHTML = 'Name: ' + qualifications[event.target.parentElement.id].name
    qualDetail.appendChild(name)

    qualDetail.style.display = 'block';
}