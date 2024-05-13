function updateFlaskMoment() {
    // This function will look for any element with class 'flask-moment'
    // and apply the Moment.js formatting based on the data attributes.
    $('.flask-moment').each(function () {
        var $this = $(this);
        var timestamp = moment($this.data('timestamp'));

        // Check for specific formatting functions like 'fromNow'
        if ($this.data('function') === 'fromNow') {
            $this.text(timestamp.fromNow());
            $this.show(); // Remove 'display: none'
        }
    });
}

$(document).ready(function () {
    $('.comment-form').submit(function (event) {
        event.preventDefault();  // Prevent the form from submitting through the browser
        var form = $(this);
        var postData = form.serialize();  // Get the form data
        var postUrl = form.attr('action');  // Get the form action
        var postId = form.find('input[name="post_id"]').val();  // Correctly get the post ID from the hidden input

        $.ajax({
            url: postUrl,
            type: 'POST',
            data: postData,
            success: function (response) {
                // Append the new comment to the appropriate comment section
                $('#comments-' + postId).append(response.comment_html);
                form.find('textarea').val('');  // Clear the text area
                // Optional: reset any other elements of the form
                updateFlaskMoment();  // Update the Moment.js formatting
            },
            error: function () {
                alert('Error posting comment.');
            }
        });
    });
});