const navitems = [
    {
        'name': 'dashboard',
        'label': 'Dashboard',
        'url': 'dash1.html',
    },
    {
        'name': 'courselist',
        'label': 'Course List',
        'url': 'courselist.html',
    },
    {
        'name': 'qualifications',
        'label': 'Qualifications',
        'url': 'qualificationlist.html',
    },
    {
        'name': 'batches',
        'label': 'Batches',
        'url': 'batches.html',
    },
]

const navheader = '<li><div class="user-view">\
<div class="background">\
    <img src="../images/books.jpg">\
</div>\
<a href="#user"><img class="circle" src="../images/profile.webp"></a>\
<a href="#name"><span class="white-text name">John Doe</span></a>\
<a href="#email"><span class="white-text email">jdandturk@gmail.com</span></a>\
</div></li>'


// navdrawer options
const options = {
    'edge': 'left'
}


// render navdrawer elements
navdr = document.getElementById('slide-out')
navdr.innerHTML = navheader
navitems.forEach(item => {
    const a = document.createElement('a')
    const li = document.createElement('li')

    li.appendChild(a)
    a.innerText = item.label
    
    if (page === item.name){
        a.href = '#'
        li.className = 'active indigo accent-1'
    }else{
        a.href = item.url
    }

    navdr.appendChild(li)
});


// navdrawer click
document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems, options);
});