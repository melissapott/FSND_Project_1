import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>
    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
        .popover {
            max-width: none;
            width: 300px;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        
//  Starter code removed:        
//  We're going to comment out this section of the script, as it causes problems when adding div's nested in the movie-tiles
//  But it came with the starter code, so we'll leave it here and just ignore it.

        // Animate in the movies when the page loads
//        $(document).ready(function () {
//          $('.movie-tile').hide().first().show("fast", function showNext() {
//            $(this).next("div").show("fast", showNext);
//          });
//       });

//  end problem section here


//this is for the detail info modal - added to starter code
       $(document).ready(function () {
	$('#detailInfoModal').on('show.bs.modal', function (event) { // id of the modal with event
	  var button = $(event.relatedTarget) // Button that triggered the modal
	  var movieTitle = button.data('movietitle') // Extract info from data-* attributes
	  var movieStoryline = button.data('storyline')
	  var movieReleaseDate = button.data('release-date')
	  var movieDirector = button.data('director')
	  var movieIMDBLink = button.data('imdb-link')
	  
	  var title = '<h2>' + movieTitle + ' : Quick Facts </h2>' //build html to display the movie title
	  var content = '<strong>Release Date:  </strong>' + movieReleaseDate + '<br>'  //build the content of the modal with html formatting
	  content = content + '<strong>Directed By:  </strong>' + movieDirector + '<br><hr>'
	  content = content + '<h3>Storyline</h3>' + movieStoryline + '<hr>'
	  content = content + '<div class=\"text-center\"> <a href=\"' + movieIMDBLink + '\"><img src=\"imdb.png\" alt=\"IMDB button\"><br>'
	  content = content + '  <small>view in IMDB for full details and more trailers</small></a></div>'
	  
	  // Update the modal's content.
	  var modal = $(this)
	  modal.find('.modal-title').html(title)
	  modal.find('.modal-body').html(content)	  

	})
        })

    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>
    <!-- Detail Info Modal  ADDED TO STARTER CODE -->
    <div class="modal fade" id="detailInfoModal" tabindex="-1" role="dialog" aria-labelledby="detailInfoModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title" id="detailnfoModalLabel">Quick Facts</h4>
          </div>
          <div class="modal-body">
            This is for the movie details
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>        
          </div>
        </div>
      </div>
    </div>
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Fresh Tomatoes Movie Trailers</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''


# A single movie entry html template
# Extra divs were added to the starter code in this section to accomodate a "more info" button, and passing
# data to another modal display
movie_tile_content = '''
<div class="col-md-6 col-lg-4" id="{movie_title}">
    <div class="movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
        <img src="{poster_image_url}" width="220" height="342">
        <h2>{movie_title}</h2>
    </div>
    <div class="movie-info text-center">
        <button type="button" class="btn btn-info" data-toggle="modal" data-target="#detailInfoModal" data-movietitle="{movie_title}"
        data-director="{director}" data-release-date="{release_date}" data-imdb-link="{imdb_link}" data-storyline="{storyline}">More Info</button>
    </div>
</div>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in (extra variables were added for project submission)
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            storyline = movie.storyline,
            director = movie.director,
            release_date = movie.release_date,
            imdb_link = movie.imdb_link
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))

   
    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
