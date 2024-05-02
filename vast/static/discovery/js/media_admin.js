// media_admin.js
(function(jQuery){
    jQuery(document).ready(function(){
        function updateFormatChoices() {
            var mediaTypeId = jQuery('#id_media_type').val();
            var formatField = jQuery('#id_format');
            var obj_id = jQuery('.form-row.field-id .readonly').text();
            // Fetch and populate choices based on the selected media type
            jQuery.ajax({
                url: '/discovery/format_choices/',
                data: {'media_type_id': mediaTypeId, 'obj_id': obj_id},
                success: function(data) {
                    formatField.empty();
                    jQuery.each(data["choices"], function(key, value) {
                        var option = jQuery('<option>', {
                            value: key,
                            text: value
                        });
                        if (key === data["selected"]) {
                            option.prop('selected', true);
                        }
                        formatField.append(option);
                    });
                }
            });
            jQuery("div.flex-container:has(label:contains('Describe label'))").hide();
            jQuery("div.flex-container:has(label:contains('Enhance label'))").hide();
            jQuery("#media_identifiers-group").show();
            jQuery('.field-format').show();
            jQuery('.field-related_media').show();
            if (mediaTypeId === 'book'){
                jQuery(".column-identifier").text('ISBN:');
                jQuery('label[for="id_origin"]').text('Year first published:');
            }
            else if (mediaTypeId === 'movie'){
                jQuery(".column-identifier").text('UPC:');
                jQuery('label[for="id_origin"]').text('Year first released:');
            }
            else if (mediaTypeId === 'tv_show'){
                jQuery(".column-identifier").text('UPC:');
                jQuery('label[for="id_origin"]').text('Year first released:');
            }
            else if (mediaTypeId === 'music'){
                jQuery(".column-identifier").text('UPC or ISRC:');
                jQuery('label[for="id_origin"]').text('Year first released:');
            }
            else if (mediaTypeId === 'podcast'){
                jQuery(".column-identifier").text('UPC:');
                jQuery('label[for="id_origin"]').text('Year first released:');
            }
            else if (mediaTypeId === 'game'){
                jQuery(".column-identifier").text('UPC:');
                jQuery('label[for="id_origin"]').text('Year first released:');
            }
            else if (mediaTypeId === 'theater'){
                jQuery("#media_identifiers-group").hide();
                jQuery('label[for="id_origin"]').text('Year first performed:');
            }
            else if (mediaTypeId === 'artifact'){
                jQuery(".column-identifier").text('Museum number:');
                jQuery('label[for="id_origin"]').text('Year created:');
            }
            else if (mediaTypeId === 'discovery'){
                jQuery('.field-format').hide();
                jQuery(".column-identifier").text('Identifier:');
                jQuery('label[for="id_origin"]').text('Year created:');
                jQuery('.field-related_media').hide();

            }
            else{
                jQuery(".column-identifier").text('Identifier:');
                jQuery('label[for="id_origin"]').text('Year created:');
            }
        }
        // Attach an event listener to the media_type field
        jQuery('#id_media_type').on('change', updateFormatChoices);

        // Initialize choices on page load
        updateFormatChoices();
    });

})(jQuery);
