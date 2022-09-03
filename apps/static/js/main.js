
// navdrawer options
const navOptions = {
    'edge': 'left'
}

// navdrawer options
const modalOptions = {
}



// navdrawer click
document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems, navOptions);
});

// Modal
document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems, modalOptions);
});


// Select
document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems, {});
});


// Pagination rows select
function pageRows(url) {
    const rows = event.target.value
    if (queryDict['search']){
        window.location.href =  url + `?rows=${rows}` + `&search=${queryDict['search']}`
    }else{
        window.location.href =  url + `?rows=${rows}`
    }
}


// Tooltips

document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.tooltipped');
    var instances = M.Tooltip.init(elems, {});
});