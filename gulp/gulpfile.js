(function() {
    'use strict';

    var source_js = './src/js/main.js',
        source_css = './src/sass/*.scss',
        dest_js = 'bundle.js',
        dest_css = 'bundle.css',
        dest_dir = './build';

    var gulp = require('gulp'),
        watchify = require('watchify'),
        browserify = require('browserify'),
        sass = require('gulp-sass'),
        cleancss = require("gulp-clean-css"),
        gzip = require("gulp-gzip"),
        concat = require('gulp-concat'),
        source = require('vinyl-source-stream');

    var gzip_options = {
        threshold: '1kb',
        gzipOptions: {
            level: 5
        }
    }

    var build_js = function() {
        return browserify(source_js)
            .bundle()
            .pipe(source(dest_js))
            .pipe(gulp.dest(dest_dir))
            .pipe(gzip(gzip_options))
            .pipe(gulp.dest(dest_dir));
    }

    var build_sass = function() {
        return gulp.src(source_css)
            .pipe(sass({
                includePaths: ['./node_modules/bootstrap-sass/assets/stylesheets'],
            }))
            .pipe(concat(dest_css))
            .pipe(gulp.dest(dest_dir))
            .pipe(gulp.dest(dest_dir))
            .pipe(cleancss())
            .pipe(gulp.dest(dest_dir))
            .pipe(gzip(gzip_options))
            .pipe(gulp.dest(dest_dir));
    }

    gulp.task('build_js', build_js);
    gulp.task('build_sass', build_sass);

    gulp.task('watch_js', function() {
        gulp.watch('./src/js/**/*.js', ['build_js']);
    });

    gulp.task('watch_sass', function() {
        gulp.watch('./src/sass/**/*.scss', ['build_sass']);
    });

    gulp.task('default', ['build_js', 'watch_js',
                          'build_sass', 'watch_sass']);

}());
