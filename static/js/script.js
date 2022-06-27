function moveNavContent() {
    let topContainer = document.getElementById('top-nav-container');
    let mobileContainer = document.getElementById('mobile-top-nav-container');
    let content = document.getElementById('account-links');
    breakpoint = 992;
    viewportWidth = window.innerWidth || document.documentElement.clientWidth;

    if (viewportWidth < breakpoint) {
        if (mobileContainer.innerHTML != content) {
            mobileContainer.appendChild(content);
            console.log('moved from if statement into mobile container');
        }
    }
    if (viewportWidth >= breakpoint) {
        if (topContainer.innerHTML != content) {
            topContainer.appendChild(content);
            console.log('moved from if statement into top container');
        }
    }
    window.addEventListener('resize', () => {
        let viewportWidth = window.innerWidth || document.documentElement.clientWidth;
        if (viewportWidth < breakpoint) {
            mobileContainer.appendChild(content);
            console.log('moved from eventlistener into mobileContainer');
        } else if (viewportWidth >= breakpoint) {
            topContainer.appendChild(content);
            console.log('moved from eventlistener into topContainer');
        }
    })
}

function displaySearch() {
    console.log('search icon clicked');
    let searchForm = document.getElementById('search-form');
    let searchFormContainer = document.getElementById('search-form-container');
    searchFormContainer.style.display = 'block';
    searchForm.style.display = 'flex';
    searchForm.addEventListener('click', (e) => {
        console.log('searchForm clicked');
        e.stopImmediatePropagation();
    })
    searchFormContainer.addEventListener('click', () => {
        console.log('searchFormContainer clicked');
        searchForm.style.display = 'none';
        searchFormContainer.style.display = 'none';
    })
}

function closeModal() {
	var container = document.getElementById("modals-here")
	// var backdrop = document.getElementById("modal-backdrop")
	var modal = document.getElementById("modal")

	modal.classList.remove("show")
	// backdrop.classList.remove("show")

	setTimeout(function() {
		// container.removeChild(backdrop)
		container.removeChild(modal)
	}, 200)
}

function stopPropagation(event) {
    event.stopImmediatePropagation()
}

let searchIcon = document.getElementById('search-container').addEventListener('click', displaySearch);
moveNavContent();
