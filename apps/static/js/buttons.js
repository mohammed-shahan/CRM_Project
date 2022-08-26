export function button(handler, text, icon, color) {
    const btn = document.createElement('a')
    btn.className = 'waves-effect waves-light btn ' + color
    btn.innerText = text
    const btnIcon = document.createElement('i')
    btnIcon.className = 'material-icons left'
    btnIcon.innerText = icon
    btn.appendChild(btnIcon)
    btn.addEventListener('click', handler)
    return btn;
}