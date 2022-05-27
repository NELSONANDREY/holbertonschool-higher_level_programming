window.addEventListener('DOMContentLoaded', function () {
    $('#add_item').click(function () {
      $('UL.my_list').append('<li>Item</li>') 
    });
    $('#remove_item').click(function(){
        $('.my_list li').last().remove();
    })
    $('#clear_list').click(function(){
        $('UL.my_list').remove();
    })
});
