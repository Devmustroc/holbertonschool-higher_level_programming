$.get('https://swapi-api.hbtn.io/api/films/?format=json', function(data) {
    let allmovies = data.results;
    for (let i = 0; i < allmovies.length; i++) {
        console.log(allmovies[i]);
        $('UL#list_movies').append('<li>'+ allmovies[i].title +'</li>');
    }
});