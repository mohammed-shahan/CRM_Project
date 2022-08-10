var batches = [
    {
        code: 'Q001',
        name: 'Batch 1',
    },
    {
        code: 'Q002',
        name: 'Batch 2',
    },
]

const table = document.getElementById('batches')

var count = 1;
batches.forEach((b, index) => {
    var row = table.insertRow(count++);
    var code = row.insertCell(0);
    var name = row.insertCell(1);

    row.id = index;
    code.innerHTML = b.code;
    name.innerHTML = b.name;

    row.addEventListener('click', viewBatches)
});

function viewBatches(event) {
    batchDetail = document.getElementById('batch-detail')
    batchDetail.innerHTML = ''

    var code = document.createElement('div')
    code.innerHTML = 'Code: ' + batches[event.target.parentElement.id].code
    batchDetail.appendChild(code)

    var name = document.createElement('div')
    name.innerHTML = 'Name: ' + batches[event.target.parentElement.id].name
    batchDetail.appendChild(name)

    batchDetail.style.display = 'block';
}