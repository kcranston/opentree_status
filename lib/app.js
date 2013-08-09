//lib/app.js

exports.views = {
    curators: {
        map: function(doc) {
            curator = doc.study_info['ot:curatorName'];
            emit(curator, null);
        }
    }
}
