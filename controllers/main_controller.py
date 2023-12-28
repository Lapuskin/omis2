from flask import Flask, render_template

from interfaces.buyer_controller_interface import BuyerControllerInterface
from interfaces.lots_controller_interface import LotsControllerInterface
from interfaces.seller_controller_Interface import SellerControllerInterface
from repo.model import db
from views.main_view import MainView


class MainController:
    def __init__(self):
        self.__app = Flask(__name__, template_folder='../templates')
        self.__seller_controller = SellerControllerInterface
        self.__buyer_controller = BuyerControllerInterface
        self.__lot_controller = LotsControllerInterface
        self.__view = MainView()
        self.db = db

    def run(self):
        self.__app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.__app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.db.init_app(self.__app)

        with self.__app.app_context():
            self.db.create_all()

            routes = self.__view.get_windows()
            @self.__app.route('/')
            def index():
                return render_template(routes['/'])

            @self.__app.route('/lot_edit')
            def lot_edit():
                return render_template(routes['/lot_edit'])

            @self.__app.route('/buyer_edit')
            def buyer_edit():
                return render_template(routes['/buyer_edit'])

            @self.__app.route('/buyer_create')
            def buyer_create():
                return render_template(routes['/buyer_create'])

            @self.__app.route('/seller_create')
            def seller_create():
                return render_template(routes['/seller_create'])

            @self.__app.route('/lot_create')
            def lot_create():
                return render_template(routes['/lot_create'])

            self.__app.run()
