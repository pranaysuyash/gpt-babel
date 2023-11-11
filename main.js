document.addEventListener('DOMContentLoaded', () => {
  const addGptButton = document.getElementById('add-gpt-button');
  const addGptModal = document.getElementById('add-gpt-modal');
  const closeButton = document.querySelector('.close-button');
  const addGptForm = document.getElementById('add-gpt-form');
  const searchBar = document.getElementById('search-bar');
  const gptListingsTableBody = document.querySelector('#gpt-listings tbody');

  // Function to open the modal
  function openModal() {
    addGptModal.style.display = 'block';
  }

  // Function to close the modal
  function closeModal() {
    addGptModal.style.display = 'none';
  }

  // Event listeners for opening and closing the modal
  addGptButton.addEventListener('click', openModal);
  closeButton.addEventListener('click', closeModal);
  window.addEventListener('click', (event) => {
    if (event.target === addGptModal) {
      closeModal();
    }
  });

  // Function to create and append a table cell
  function addCell(row, text) {
    const cell = document.createElement('td');
    cell.textContent = text;
    row.appendChild(cell);
  }

  // Function to create and append a cell with an image
  function addCellWithImage(row, imgUrl) {
    const imgCell = document.createElement('td');
    const img = new Image();
    img.src = imgUrl;
    img.alt = 'GPT Logo';
    img.style.width = '50px'; // Set image size as needed
    img.style.height = 'auto';
    imgCell.appendChild(img);
    row.appendChild(imgCell);
  }

  // Function to create and append a cell with a hyperlink
  function addCellWithLink(row, url) {
    const linkCell = document.createElement('td');
    const link = document.createElement('a');
    link.href = url;
    link.target = '_blank';
    const icon = document.createElement('i');
    icon.className = 'fa fa-external-link'; // Assuming you're using Font Awesome
    link.appendChild(icon);
    linkCell.appendChild(link);
    row.appendChild(linkCell);
  }

  // Function to update event listings with new data
  function updateEventListings(data) {
    // Clear existing listings if needed
    gptListingsTableBody.innerHTML = '';

    // Add new data row
    const row = gptListingsTableBody.insertRow();
    addCellWithImage(row, data.display.profile_picture_url); // GPT Logo
    addCell(row, data.display.name); // GPT Name
    addCell(row, data.author.display_name); // Created by
    addCell(row, data.display.description); // Description
    addCell(row, data.display.prompt_starters.join(', ')); // Prompt Starter Messages
    addCell(row, data.display.welcome_message); // Welcome Message
    addCellWithLink(row, `https://chat.openai.com/g/${data.short_url}`); // View GPT
  }

  // Event listener for the form submission
  addGptForm.addEventListener('submit', (event) => {
    event.preventDefault();
    const url = document.getElementById('url').value;

    fetch('http://127.0.0.1:5000/submit-url', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ url: url }),
    })
      .then((response) => response.json())
      .then((data) => {
        if (!data.error) {
          updateEventListings(data);
          closeModal();
        } else {
          console.error('Error:', data.error);
        }
      })
      .catch((error) => {
        console.error('Fetch error:', error);
      });
  });

  // Event listener for the search bar
  searchBar.addEventListener('input', (event) => {
    const searchTerm = event.target.value.toLowerCase();

    Array.from(gptListingsTableBody.rows).forEach((row) => {
      const isVisible = Array.from(row.cells).some((cell) =>
        cell.textContent.toLowerCase().includes(searchTerm)
      );
      row.style.display = isVisible ? '' : 'none';
    });
  });
});
