import { button } from "/static/js/buttons.js";


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


function showQualifications() {
    const tbody = document.getElementById('qual-tbody')
    tbody.innerHTML = ''

    qualifications.forEach((q, index) => {
        var row = document.createElement('tr')
        var code = row.insertCell(0);
        var name = row.insertCell(1);
        var actions = row.insertCell(2);
        actions.className = 'actions';
    
        code.innerHTML = q.code;
        name.innerHTML = q.name;

        const editBtn = button(editQual, 'Edit', 'edit', 'indigo accent-4');
        const deleteBtn = button(deleteQual, 'Delete', 'delete', 'red')

        actions.appendChild(editBtn);
        actions.appendChild(deleteBtn);

        row.id = index;

        tbody.appendChild(row);
    });    
}

function deleteQual() {
    const id = event.target.parentElement.parentElement.id;
    
    if(confirm(`You sure you want to delete ${qualifications[id].code}: ${qualifications[id].name}?`)){
        delete qualifications[id];
        showQualifications();
    }
}

function editQual(event) {
    const id = event.target.parentElement.parentElement.id;
    var modal = M.Modal.getInstance(document.getElementById('edit-qual-modal'));

    const txtName = document.getElementById('txtEditName');
    const txtCode = document.getElementById('txtEditCode');
    const txtId = document.getElementById('txtEditId');

    txtName.value = qualifications[id].name;
    txtCode.value = qualifications[id].code;
    txtId.value = id;

    modal.open()
}

function addQualConfirm() {
    var modal = M.Modal.getInstance(document.getElementById('add-qual-modal'));
    const txtName = document.getElementById('txtAddName');
    const txtCode = document.getElementById('txtAddCode');
    
    if (txtCode.value === ''){
        alert('Code cannot be empty!');
        return
    }
    if (txtName.value === ''){
        alert('Name cannot be empty!');
        return
    }

    qualifications.push({
        code: txtCode.value,
        name: txtName.value
    })

    txtCode.value = ''
    txtName.value = ''

    showQualifications();

    modal.close();
}

function editQualConfirm() {
    var modal = M.Modal.getInstance(document.getElementById('edit-qual-modal'));
    const txtName = document.getElementById('txtEditName');
    const txtCode = document.getElementById('txtEditCode');
    const id = Number(document.getElementById('txtEditId').value);
    
    if (txtCode.value === ''){
        alert('Code cannot be empty!');
        return
    }
    if (txtName.value === ''){
        alert('Name cannot be empty!');
        return
    }

    qualifications[id].code = txtCode.value;
    qualifications[id].name = txtName.value;

    txtCode.value = ''
    txtName.value = ''

    showQualifications();

    modal.close();
}

function addQualCancel() {
    const txtName = document.getElementById('txtAddName');
    const txtCode = document.getElementById('txtAddCode');

    txtCode.value = '';
    txtName.value = '';
}


showQualifications();

window.addQualCancel = addQualCancel;
window.editQualConfirm = editQualConfirm;
window.addQualConfirm = addQualConfirm;