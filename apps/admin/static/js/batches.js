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
    batchDetailContent = document.createElement('div')
    batchDetailContent.className = 'card-content'
    batchDetail.appendChild(batchDetailContent)

    var code = document.createElement('div')
    code.innerHTML = 'Code: ' + batches[event.target.parentElement.id].code
    batchDetailContent.appendChild(code)

    var name = document.createElement('div')
    name.innerHTML = 'Name: ' + batches[event.target.parentElement.id].name
    batchDetailContent.appendChild(name)

    batchDetail.style.display = 'block';
}