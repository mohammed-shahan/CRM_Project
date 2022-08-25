
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