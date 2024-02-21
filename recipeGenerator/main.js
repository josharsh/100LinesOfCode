document.getElementById('searchBtn').addEventListener('click', function () {
    var ingredients = document.getElementById('ingredientInput').value;
    var searchIngredients = ingredients.split(',');
    recipee(searchIngredients);
});

async function recipee(ingredient) {
    try {
        var data = await fetchRecipe(ingredient);
        if (data) {
            let result = document.getElementById('results');
            let html = '';

            data.forEach(function (recipe) {
                html += '<div class="recipee">';
                html += '<div class="top">';
                html += '<img src="' + recipe.image + '" alt="" />';
                html += '</div>';
                html += '<div class="bottom">';
                html += '<div class="recipee-name">';
                html += '<h2>' + recipe.title + '</h2>';
                html += '<p class="likes">💖 : ' + recipe.likes + '</p>';
                html += '</div>';
                html += '<h3>Missed Ingredients:</h3>';
                html += '<ul class="recipee-ing">';
                recipe.missedIngredients.forEach(function (item) {
                    html += '<li>' + item.name + '<ul><li>' + item.original + '</li><img src="' + item.image + '" alt="" /></ul></li>';
                });
                html += '</ul>';
                html += '<h3>Used Ingredients:</h3>';
                html += '<ul class="recipee-ing">';
                recipe.usedIngredients.forEach(function (item) {
                    html += '<li>' + item.name + '<ul><li>' + item.original + '</li><img src="' + item.image + '" alt="" /></ul></li>';
                });
                html += '</ul>';
                html += '</div></div>';
            });

            result.innerHTML = html;
        } else {
            console.log('No data available');
        }


    } catch (error) {
        console.log('Error fetching data' + error);
    }
}

async function fetchRecipe(ingredients) {
    const apikey = 'a50c8920dc474a6788ac68f05d8c0f29'
    const url = 'https://api.spoonacular.com/recipes/findByIngredients?ingredients=' + ingredients + '&number=10&apiKey=' + apikey;
    try {
        const response = await fetch(url, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        });
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching data: ', error);
    }
}