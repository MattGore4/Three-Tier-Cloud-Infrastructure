//Listens for user document searches 
document.getElementById('search-form').addEventListener('submit', async function(e) {
    e.preventDefault();
    //Store the user query and references to the HTML elements where the results and loading text will be displayed.
    const query = document.getElementById('search-input').value;
    const resultsContainer = document.getElementById('results-container');
    const loadingIndicator = document.getElementById('loading-indicator');

    // Clear previous results and show loading indicator
    resultsContainer.innerHTML = '';
    loadingIndicator.classList.remove('hidden');

    try {
        //This sends the users query to the backend
        const response = await fetch(`/api/search?q=${encodeURIComponent(query)}`);
        //Pauses the script until the response is fully converted to JSON object
        const data = await response.json();

        //Remove loading indicator
        loadingIndicator.classList.add('hidden');

        //Ensure backend returned array of document results
        if (data.results && data.results.length > 0) {
            //Loop through documents
            data.results.forEach(result => {

                //Strip out markdown syntax for a readable document preview
                let cleanSnippet = result.snippet.replace(/[#*`]/g, '').replace(/\s+/g, ' ').trim();

                // Document card HTML with dynamically injected properties of the document
                let cardHtml = `
                    <div class="result-card" style="border-left: 4px solid #0056b3; padding: 15px; margin-bottom: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); background: white; border-radius: 4px;">
                        <h3 style="color: #0056b3; margin-top: 0;">${result.title}</h3>
                        <p style="color: #666; font-size: 0.9em; font-weight: bold;">Category: ${result.category}</p>
                        <p style="color: #333;">${cleanSnippet}</p>

                        <a href="/document.html?id=${result.id}" style="display: inline-block; margin-top: 10px; padding: 8px 16px; background-color: #0056b3; color: white; text-decoration: none; border-radius: 4px; font-size: 0.9em;">Read Full Guide &rarr;</a>
                    </div>
                `;
                resultsContainer.innerHTML += cardHtml;
            });
        //If the array is empty, inform the user no documents were found
        } else {
            resultsContainer.innerHTML = '<p>No results found for your query.</p>';
        }
    //Prints an error message if the fetch fails
    } catch (error) {
        loadingIndicator.classList.add('hidden');
        resultsContainer.innerHTML = `<p style="color: red;">Error fetching results: ${error.message}</p>`;
    }
});
