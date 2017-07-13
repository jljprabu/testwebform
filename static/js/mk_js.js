
semantic = {};
// ready event
semantic.ready = function() {

  // selector cache
  var
    $buttons = $('.ui.buttons .button'),
    $toggle  = $('.main .ui.toggle.button'),
    $button  = $('.ui.button').not($buttons).not($toggle),
    // alias
    handler = {

      activate: function() {
        $(this)
          .addClass('active')
          .siblings()
          .removeClass('active')
        ;
      }

    }
  ;

  $buttons
    .on('click', handler.activate)
  ;


// attach ready event
$(document)
  .ready(semantic.ready)
;