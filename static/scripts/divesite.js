$('#avg-rating').raty({
        starType: 'i',
        readOnly: true,
        score: $(this).attr("data-score")
    });

    $('.all-reviews').raty({
        starType: 'i',
        readOnly: true,
    });

    $('#user-rating').raty({
        starType: 'i',
        click: function(score, evt){
            $.ajax({
                url: $(this).attr("data-url"),
                method: 'POST',
                data: {
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                    divesite_id: $(this).attr("data-id"),
                    rating: score,
                },
                success: function(response){
                    console.log(response.avg_rating);
                    $('#avg-rating').raty('set', {'score': response.avg_rating});
                }
            })
         }
    });

    $("#comment-submit").click(function(){
        $.ajax({
            url: $(this).attr("data-url"),
                method: 'POST',
                data: {
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                    divesite_id: $(this).attr("data-id"),
                    comment: $("#comment").val(),
                },
                success: function(response){
                    location.reload()
                }
        })
    })

    $("#add-my-list").click(function(){
        $.ajax({
            url: $(this).attr("data-url"),
                method: 'POST',
                data: {
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                    divesite_id: $(this).attr("data-id"),
                },
                success: function(response){
                    $("#alert-success").html("Successfully Added to Future Dive List");
                    $("#alert-success").show();
                    setTimeout(function(){
                        $("#alert-success").hide();
                    }, 1000)

                }
        })
    })