function disableButton(button) {
    button.disabled = true;
}

function enableButton(button) {
    button.disabled = false;
}

// listens for click events on specific buttons to prevent multiple instances of same form being open at the same time
document.addEventListener('click', (event) => {
    if (event.target.disabled){
        return;
    } else if (event.target.id == 'add-category-btn') {
        setTimeout(function() {
            addBtn = document.getElementById('add-category-btn');
            editBtns = document.getElementsByClassName('edit-category-btn');
            deleteBtns = document.getElementsByClassName('delete-category-btn');
            for (let i = 0; i < editBtns.length; i++){
                disableButton(editBtns[i]);
            }
            for (let i = 0; i < deleteBtns.length; i++){
                disableButton(deleteBtns[i]);
            }
            disableButton(addBtn);
        }, 300);
    } else if (event.target.classList.contains('edit-category-btn') || event.target.classList.contains('delete-category-btn')) {
        setTimeout(function() {
            addBtn = document.getElementById('add-category-btn');
            deleteBtns = document.getElementsByClassName('delete-category-btn');
            editBtns = document.getElementsByClassName('edit-category-btn');
            for (let i= 0; i < deleteBtns.length; i++){
                disableButton(deleteBtns[i]);
            }
            for (let i= 0; i < editBtns.length; i++){
                disableButton(editBtns[i]);
            }
            disableButton(addBtn);
        }, 300);
    } else if (event.target.id == 'save-btn-add-category' || event.target.id == 'cancel-btn-add-category') {
        setTimeout(function() {
            addBtn = document.getElementById('add-category-btn');
            editBtns = document.getElementsByClassName('edit-category-btn');
            deleteBtns = document.getElementsByClassName('delete-category-btn');
            for (let i= 0; i < editBtns.length; i++){
                enableButton(editBtns[i]);
            }
            for (let i= 0; i < deleteBtns.length; i++){
                enableButton(deleteBtns[i]);
            }
            enableButton(addBtn);
        }, 300);
    } else if (event.target.id == 'save-btn-add-category' || event.target.id == 'delete-category-cancel' || event.target.id == 'cancel-btn-add-category' || event.target.id == 'delete-category-confirm') {
        setTimeout(function() {
            addBtn = document.getElementById('add-category-btn');
            deleteBtns = document.getElementsByClassName('delete-category-btn');
            editBtns = document.getElementsByClassName('edit-category-btn');
            for (let i= 0; i < editBtns.length; i++){
                enableButton(editBtns[i]);
            }
            for (let i= 0; i < deleteBtns.length; i++){
                enableButton(deleteBtns[i]);
            }
            enableButton(addBtn);
        }, 300);
    } else if (event.target.id == 'cancel-btn-edit-category' || event.target.id == 'save-btn-edit-category') {
        setTimeout(function() {    
            addBtn = document.getElementById('add-category-btn');
            deleteBtns = document.getElementsByClassName('delete-category-btn');
            editBtns = document.getElementsByClassName('edit-category-btn');
            for (let i= 0; i < editBtns.length; i++){
                enableButton(editBtns[i]);
            }
            for (let i= 0; i < deleteBtns.length; i++){
                enableButton(deleteBtns[i]);
            }
            enableButton(addBtn);
        }, 300);
    }
})