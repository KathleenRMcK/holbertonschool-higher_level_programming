$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
  $.each(data.results, function (index, film) {
    $('ul#list_movies').append('<li>' + film.title + '</li>');
  });
});
