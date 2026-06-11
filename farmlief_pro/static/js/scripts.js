// Get all tab-link elements
const tabLinks = document.querySelectorAll('.tab-link');

// Add click event listener to each tab-link
tabLinks.forEach(tabLink => {
  tabLink.addEventListener('click', function() {
    // Remove tab-active class from all tab-links
    tabLinks.forEach(link => link.classList.remove('tab-active'));
    
    // Add tab-active class to the clicked tab-link
    this.classList.add('tab-active');
  });
});