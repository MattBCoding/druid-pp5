// function to handle moving the nav content around depending on screen size
function moveNavContent() {
    let topContainer = document.getElementById('top-nav-container');
    let mobileContainer = document.getElementById('mobile-top-nav-container');
    let content = document.getElementById('account-links');
    let breakpoint = 992;
    let viewportWidth = window.innerWidth || document.documentElement.clientWidth;

    if (viewportWidth < breakpoint) {
        if (mobileContainer.innerHTML != content) {
            mobileContainer.appendChild(content);
        }
    }
    if (viewportWidth >= breakpoint) {
        if (topContainer.innerHTML != content) {
            topContainer.appendChild(content);
        }
    }
    window.addEventListener('resize', () => {
        let viewportWidth = window.innerWidth || document.documentElement.clientWidth;
        if (viewportWidth < breakpoint) {
            mobileContainer.appendChild(content);
        } else if (viewportWidth >= breakpoint) {
            topContainer.appendChild(content);
        }
    });
}

// function to display the search box on request
function displaySearch() {
    let searchForm = document.getElementById('search-form');
    let searchFormContainer = document.getElementById('search-form-container');
    searchFormContainer.style.display = 'block';
    searchForm.style.display = 'flex';
    searchForm.addEventListener('click', (e) => {
        e.stopImmediatePropagation();
    });
    searchFormContainer.addEventListener('click', () => {
        searchForm.style.display = 'none';
        searchFormContainer.style.display = 'none';
    });
}

// function to close modal inserted by htmx
function closeModal() {
	var container = document.getElementById("modals-here");
	var modal = document.getElementById("modal");

	modal.classList.remove("show");

	setTimeout(function() {
		container.removeChild(modal);
	}, 200);
}

// function to prevent click through modal inserted by htmx
function stopPropagation(event) {
    event.stopImmediatePropagation();
}

let searchIcon = document.getElementById('search-container').addEventListener('click', displaySearch);
moveNavContent();
