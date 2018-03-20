$(".remove-favorite").click(function(e){
		e.preventDefault();
		$.post({
			url: $(this).attr('href'),
			data: {
			csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
			},
			success: function(){
				location.reload()
			}
		})
	})

	$("#delete-account").click(function(){
        $.ajax({
            url: $(this).attr("data-url"),
                method: 'POST',
                data: {
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                    user: $(this).attr(data-user),
                },
                success: function(response){
					location.reload()

                }
        })
    })