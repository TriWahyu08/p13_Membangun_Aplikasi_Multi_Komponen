# services.py
from abc import ABC, abstractmethod
import logging
from models import Product, CartItem # Wajib diimpor dari models.py
from typing import List

LOGGER = logging.getLogger('SERVICES')

# --- INTERFACE PEMBAYARAN (Diperlukan untuk DIP/OCP) ---
class IPaymentProcessor(ABC):
    @abstractmethod
    def process(self, amount: float) -> bool:
        pass

# --- IMPLEMENTASI PEMBAYARAN TUNAI ---
class CashPayment(IPaymentProcessor):
    def process(self, amount: float) -> bool:
        LOGGER.info(f"Menerima TUNAI sejumlah: Rp{amount:,.0f}")
        return True
    
# Menambahkan kode baru setelah Class CashPayment
# --- IMPLEMENTASI PEMBAYARAN KARTU DEBIT ---
class DebitCardPayment(IPaymentProcessor):
    def process(self, amount: float) -> bool:
        LOGGER.info(f"Memproses pembayaran Kartu DEBIT sejumlah: Rp{amount:,.0f}")
        # Logika simulasi pembayaran kartu debit
        return True # Asumsikan selalu sukses dalam simulasi ini

# --- SERVICE KERANJANG BELANJA (Logika Inti Bisnis) ---
class ShoppingCart:
    """Mengelola item, kuantitas, dan total harga pesanan (SRP)."""
    def __init__(self):
        self._items: dict[str, CartItem] = {}

    def add_item(self, product: Product, quantity: int = 1):
        if product.id in self._items:
            self._items[product.id].quantity += quantity
        else:
            self._items[product.id] = CartItem(product=product, quantity=quantity)
        LOGGER.info(f"Added {quantity}x {product.name} to cart.")

    def get_items(self) -> list[CartItem]:
        return list(self._items.values())

    @property
    def total_price(self) -> float:
        return sum(item.subtotal for item in self._items.values())
    