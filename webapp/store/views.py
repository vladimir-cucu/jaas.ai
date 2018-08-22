from flask import Blueprint, abort, render_template
from webapp.store import models


jaasstore = Blueprint(
  'jaasstore', __name__,
  template_folder='/templates', static_folder='/static')


@jaasstore.route('/store')
def store():
    return render_template('store/store.html')


@jaasstore.route('/u/<user_name>/<entity_name>/<series>/<version>')
def user_details_series_version():
    raise NotImplementedError()


@jaasstore.route('/u/<user_name>/<entity_name>/<series>')
def user_details_series():
    raise NotImplementedError()


@jaasstore.route('/u/<user_name>/<entity_name>/')
def user_details():
    raise NotImplementedError()


@jaasstore.route('/<charm_or_bundle_name>/<series>/<version>')
def details_with_series_version(charm_or_bundle_name, series, version):
    charm_or_bundle = models.get_charm_or_bundle_with_series_version(
        charm_or_bundle_name,
        series,
        version,
    )

    if charm_or_bundle:
        if charm_or_bundle['is_charm']:
            return render_template(
                'store/charm-details.html',
                context={'charm': charm_or_bundle}
            )
        else:
            return render_template(
                'store/bundle-details.html',
                context={'bundle': charm_or_bundle}
            )
    else:
        return abort(404, "Entity not found {}".format(charm_or_bundle_name))


@jaasstore.route('/<charm_or_bundle_name>/<series>')
def details_with_series(charm_or_bundle_name, series):
    charm_or_bundle = models.get_charm_or_bundle_with_series(
        charm_or_bundle_name,
        series
    )

    if charm_or_bundle:
        if charm_or_bundle['is_charm']:
            return render_template(
                'store/charm-details.html',
                context={'charm': charm_or_bundle}
            )
        else:
            return render_template(
                'store/bundle-details.html',
                context={'bundle': charm_or_bundle}
            )
    else:
        return abort(404, "Entity not found {}".format(charm_or_bundle_name))


@jaasstore.route('/<charm_or_bundle_name>')
def details(charm_or_bundle_name):
    charm_or_bundle = models.get_charm_or_bundle(charm_or_bundle_name)

    if charm_or_bundle:
        if charm_or_bundle['is_charm']:
            return render_template(
                'store/charm-details.html',
                context={'charm': charm_or_bundle}
            )
        else:
            return render_template(
                'store/bundle-details.html',
                context={'bundle': charm_or_bundle}
            )
    else:
        return abort(404, "Entity not found {}".format(charm_or_bundle_name))
