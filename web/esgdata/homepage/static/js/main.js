// Navigation Functions
function toggleMenu() {
    const sidebar = document.getElementById('sidebar');
    const content = document.getElementById('mainContent');
    sidebar.classList.toggle('collapsed');
    content.classList.toggle('collapsed');
}

function showSection(sectionId) {
    console.log('Showing section:', sectionId);
    // Hide all sections
    const sections = document.querySelectorAll('.section');
    sections.forEach(section => {
        section.style.display = 'none';
        section.classList.remove('active');
    });

    // Show the selected section
    const selectedSection = document.getElementById(sectionId);
    if (selectedSection) {
        selectedSection.style.display = 'block';
        selectedSection.classList.add('active');
    }

    // On mobile, close the sidebar after section selection
    if (window.innerWidth <= 768) {
        toggleMenu();
    }
}

// Template Grid Pagination
const itemsPerPage = 2;
let currentPage = 1;
const items = document.querySelectorAll('.image-item');
const totalPages = Math.ceil(items.length / itemsPerPage);

function showPage(page) {
    const startIndex = (page - 1) * itemsPerPage;
    const endIndex = startIndex + itemsPerPage;

    items.forEach((item, index) => {
        item.style.display = 'none';
    });

    for (let i = startIndex; i < endIndex && i < items.length; i++) {
        items[i].style.display = 'block';
    }

    document.getElementById('prevBtn').style.display = page > 1 ? 'inline-block' : 'none';
    document.getElementById('nextBtn').style.display = page < totalPages ? 'inline-block' : 'none';
}

function changePage(direction) {
    currentPage += direction;
    if (currentPage < 1) currentPage = 1;
    if (currentPage > totalPages) currentPage = totalPages;
    showPage(currentPage);
}

// Modal Functions
function openModal(imageSrc) {
    const modal = document.getElementById('imageModal');
    const modalImage = document.getElementById('modalImage');
    modalImage.src = imageSrc;
    new bootstrap.Modal(modal).show();
}

function closeModal() {
    const modal = document.getElementById('imageModal');
    bootstrap.Modal.getInstance(modal).hide();
}


 document.addEventListener("DOMContentLoaded", function () {
        // Fetch scope and category dropdown values
        fetch('/api/get-scopes-categories/')
            .then(response => response.json())
            .then(data => {
                let scopeDropdown = document.getElementById("scope-dropdown");
                let categoryDropdown = document.getElementById("category-dropdown");

                data.scopes.forEach(scope => {
                    let option = new Option(scope, scope);
                    scopeDropdown.add(option);
                });

                data.categories.forEach(category => {
                    let option = new Option(category, category);
                    categoryDropdown.add(option);
                });
            });

        // Handle form submission
        document.getElementById("filter-form").addEventListener("submit", function (e) {
            e.preventDefault();

            let scope = document.getElementById("scope-dropdown").value;
            let category = document.getElementById("category-dropdown").value;

            let queryString = `?scope=${encodeURIComponent(scope)}&category=${encodeURIComponent(category)}`;
            fetch('/api/filter-attributes/' + queryString)
                .then(response => response.json())
                .then(data => {
                    let tableBody = document.querySelector("#attributes-table tbody");
                    tableBody.innerHTML = ""; // Clear table

                    data.attributes.forEach(attr => {
                        let row = tableBody.insertRow();
                        row.innerHTML = `
                            <td>${attr.attribute_name}</td>
                            <td>${attr.measuring_unit}</td>
                            <td>${attr.GWP_factor}</td>
                            <td>${attr.scope}</td>
                            <td>${attr.category}</td>
                            <td><input type="number" name="value_${attr.attribute_name}" /></td>
                        `;
                    });
                });
        });
    });

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    // Initialize pagination
    showPage(currentPage);
    // Show the first section by default
    showSection('section1');

    // Add click event listeners to all navigation links
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const sectionId = this.getAttribute('onclick').match(/'([^']+)'/)[1];
            showSection(sectionId);
        });
    });

    // Standards Table Functionality
    const isoStandardSelect = document.getElementById('iso-standard-select');
    const releaseDateSelect = document.getElementById('release-date-select');
    const sectorSelect = document.getElementById('sector-select');
    const esgComponentSelect = document.getElementById('esg-component-select');
    const tableBody = document.querySelector('#standards-table tbody');

    // Fetch dropdown values
    fetch('/api/dropdowns/')
        .then(response => response.json())
        .then(data => {
            populateDropdown(isoStandardSelect, data.iso_standards);
            populateDropdown(releaseDateSelect, data.release_dates);
            populateDropdown(sectorSelect, data.sectors);
            populateDropdown(esgComponentSelect, data.esg_components);
        })
        .catch(error => {
            console.error('Error fetching dropdown values:', error);
            showError('Failed to load filter options');
        });

    function populateDropdown(select, values) {
        values.forEach(item => {
            const option = document.createElement('option');
            option.value = item.value;
            option.textContent = item.label;
            select.appendChild(option);
        });
    }

    function updateTable() {
        const query = new URLSearchParams({
            iso_standard: isoStandardSelect.value,
            release_date: releaseDateSelect.value,
            sector: sectorSelect.value,
            esg_component: esgComponentSelect.value,
        });

        fetch(`/api/filter_standards/?${query.toString()}`)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                tableBody.innerHTML = '';
                data.forEach(item => {
                    const row = document.createElement('tr');
                    row.innerHTML = `
                        <td>${item.iso_standard}</td>
                        <td>${item.release_date}</td>
                        <td>${item.sector}</td>
                        <td>${item.esg_component}</td>
                    `;
                    tableBody.appendChild(row);
                });
            })
            .catch(error => {
                console.error('Error fetching table data:', error);
                showError('Failed to load standards data');
            });
    }

    function showError(message) {
        const alertDiv = document.createElement('div');
        alertDiv.className = 'alert alert-danger';
        alertDiv.textContent = message;
        tableBody.parentElement.insertBefore(alertDiv, tableBody);
        setTimeout(() => alertDiv.remove(), 5000);
    }

    // Add event listeners to dropdowns
    [isoStandardSelect, releaseDateSelect, sectorSelect, esgComponentSelect].forEach(select => {
        select.addEventListener('change', updateTable);
    });
});

document.addEventListener("DOMContentLoaded", function () {
    const toolButtons = document.querySelectorAll(".tool-btn");

    toolButtons.forEach(button => {
        button.addEventListener("click", function () {
            const selectedTool = this.getAttribute("data-tool");

            // Hide all sections
            document.getElementById("Carbon-calculator").style.display = "none";
            document.getElementById("materiality-assessment").style.display = "none";
            document.getElementById("other-esg-tools").style.display = "none";

            // Show the selected section
            document.getElementById(selectedTool).style.display = "block";

            // Reset button styles
            toolButtons.forEach(btn => btn.classList.remove("active"));

            // Highlight the clicked button
            this.classList.add("active");
			
			 if (selectedTool === "materiality-assessment") {
                attachStartAssessmentListener();
            }
        });
    });

    // Set the default active button (Carbon Calculator)
    document.querySelector("[data-tool='Carbon-calculator']").classList.add("active");
});

  function attachStartAssessmentListener() {
        const startBtn = document.getElementById("startAssessment");
        if (!startBtn) return;

        // Remove previous event listener (if any)
        startBtn.replaceWith(startBtn.cloneNode(true));
        document.getElementById("startAssessment").addEventListener("click", fetchMaterialityData);
    }
	
document.addEventListener("DOMContentLoaded", function () {
    const startAssessmentBtn = document.getElementById("startAssessment");
    const materialityContainer = document.getElementById("materiality-assessment-container");

    // Hide materiality container initially
    materialityContainer.style.display = "none";

    startAssessmentBtn.addEventListener("click", function () {
        materialityContainer.style.display = "block"; // Show container when clicked
        fetchMaterialityData(); // Fetch data when button is clicked
    });
});

function fetchMaterialityData() {
    console.log("Fetching materiality data...");
    fetch("/get-materiality-data/")
        .then(response => response.json())
        .then(data => {
            console.log("Received data:", data);
            const container = document.getElementById("indicatorContainer");
            if (!container) return;

            container.innerHTML = ""; // Clear previous content

            fetch("/get-selected-materiality/")
                .then(response => response.json())
                .then(selectedData => {
                    console.log("Pre-selected values:", selectedData);

                    Object.entries(data.data).forEach(([indicator, attributes]) => {
                        let indicatorDiv = document.createElement("div");
                        indicatorDiv.classList.add("indicator-block", "p-3", "rounded", "border", "shadow-sm");
                        indicatorDiv.innerHTML = `
                            <div class="indicator-header d-flex justify-content-between align-items-center">
                                <strong>${indicator}</strong>
                                <span class="toggle-icon">➕</span>
                            </div>
                            <div class="attribute-container d-flex flex-wrap gap-2 mt-2"></div>
                        `;

                        let attributeContainer = indicatorDiv.querySelector(".attribute-container");
                        let toggleIcon = indicatorDiv.querySelector(".toggle-icon");

                        attributeContainer.style.display = "none";

                        toggleIcon.addEventListener("click", function () {
                            if (attributeContainer.style.display === "none") {
                                attributeContainer.style.display = "flex";
                                toggleIcon.textContent = "➖";
                            } else {
                                attributeContainer.style.display = "none";
                                toggleIcon.textContent = "➕";
                            }
                        });

                        attributes.forEach(attr => {
                            let attrDiv = document.createElement("div");
                            attrDiv.classList.add("attribute-block", "p-2", "border", "rounded", "selectable");
                            attrDiv.textContent = attr;

                            if (selectedData.selected_attributes.includes(attr)) {
                                attrDiv.classList.add("selected");
                            }

                            attrDiv.addEventListener("click", function (event) {
                                this.classList.toggle("selected");
                                event.stopPropagation();
                            });

                            attributeContainer.appendChild(attrDiv);
                        });

                        container.appendChild(indicatorDiv);
                    });

                    if (!document.getElementById("submitSelection")) {
                        let submitBtn = document.createElement("button");
                        submitBtn.id = "submitSelection";
                        submitBtn.textContent = "Submit Selection";
                        submitBtn.classList.add("btn", "mt-3", "submit-btn");
                        submitBtn.addEventListener("click", submitSelections);
                        container.appendChild(submitBtn);
                    }
                })
                .catch(error => console.error("Error fetching selected materiality data:", error));
        })
        .catch(error => console.error("Error fetching materiality data:", error));
}

function submitSelections() {
    let selectedData = {};

    // Find all selected indicators
    document.querySelectorAll(".indicator-block").forEach(indicatorDiv => {
        let indicatorName = indicatorDiv.querySelector("strong").textContent.trim();
        let selectedAttributes = [];

        // Find selected attributes within this indicator
        indicatorDiv.querySelectorAll(".attribute-block.selected").forEach(attrDiv => {
            selectedAttributes.push(attrDiv.textContent.trim());
        });

        // Only include indicators that have at least one selected attribute
        if (selectedAttributes.length > 0) {
            selectedData[indicatorName] = selectedAttributes;
        }
    });

    // **Debugging: Log what is being sent**
    console.log("Sending data to backend:", JSON.stringify({ selections: selectedData }));

    fetch("/submit-materiality-selection/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ selections: selectedData })
    })
    .then(response => response.json())
    .then(data => {
        alert("Selection saved successfully!");
        console.log("Saved response:", data);
    })
    .catch(error => console.error("Error saving selections:", error));
}


// Styling for selection
let style = document.createElement("style");
style.innerHTML = `
    .indicator-block {
        background: #f8f9fa;
        cursor: pointer;
        border-left: 5px solid transparent;
        transition: all 0.3s ease-in-out;
        padding: 12px;
        border-radius: 8px;
        margin-bottom: 10px;
    }
    .indicator-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        cursor: pointer;
    }
    .toggle-icon {
        font-size: 20px;
        font-weight: bold;
        color: var(--primary-color, #007bff);
        cursor: pointer;
    }
    .attribute-container {
        display: none;
        padding-top: 5px;
        transition: all 0.3s ease-in-out;
    }
    .attribute-block {
        cursor: pointer;
        transition: all 0.3s;
        padding: 8px;
        border-radius: 6px;
        border: 1px solid var(--primary-color, #17a2b8);
        color: white;
        background: var(--primary-color, #17a2b8);
    }
    .attribute-block.selected {
        background: #ff8c00; /* Orange for selected */
        color: white;
    }
    .attribute-block:hover {
        background: #ffa500; /* Lighter orange */
        color: white;
    }
    .submit-btn {
        background: var(--primary-color, #28a745);
        border: none;
        color: white;
        padding: 10px 20px;
        border-radius: 6px;
        font-weight: bold;
        transition: all 0.3s ease-in-out;
    }
    .submit-btn:hover {
        background: var(--primary-color, #218838);
    }
`;
document.head.appendChild(style);


document.addEventListener("DOMContentLoaded", function () {
    const createMaterialBtn = document.getElementById("createMaterial");
    const customMaterialForm = document.getElementById("customMaterialForm");
    const submitCustomMaterialBtn = document.getElementById("submitCustomMaterial");

    // Show the custom material form when clicking "Create Custom Material"
    createMaterialBtn.addEventListener("click", function () {
        customMaterialForm.style.display = "block";
    });

    // Handle submission of the custom material
    submitCustomMaterialBtn.addEventListener("click", function () {
        const indicator = document.getElementById("customIndicator").value.trim();
        const attribute = document.getElementById("customAttribute").value.trim();
        const measuring_unit = document.getElementById("measuringUnit").value.trim();
        const category = document.getElementById("category").value.trim();

        if (indicator === "" || attribute === "") {
            alert("Please enter both an indicator and an attribute.");
            return;
        }

        // Send data to the backend
        fetch("/add-custom-material/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ indicator: indicator, attribute: attribute,measuring_unit:measuring_unit,category:category })
        })
        .then(response => response.json())
        .then(data => {
            if (data.message) {
                alert(data.message); // Show success message
                document.getElementById("customIndicator").value = "";
                document.getElementById("customAttribute").value = "";
                customMaterialForm.style.display = "none";

                // Refresh materiality assessment
                fetchMaterialityData();
            } else {
                alert("Error: " + data.error);
            }
        })
        .catch(error => console.error("Error adding custom material:", error));
    });
});
