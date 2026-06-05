import json
import random
import string
import datetime
from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="NeoBank – Digital Banking",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ══════════════════════════════════════════════════════════════
#  GLOBAL CSS  —  Deep Navy + Royal Blue professional scheme
# ══════════════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

/* ── Base ─────────────────────────────────── */
*, *::before, *::after { box-sizing: border-box; }
html, body, [class*="css"], .stApp {
    font-family: 'Inter', system-ui, sans-serif !important;
    background: #f0f4f8 !important;
    color: #0f172a !important;
}
.block-container { padding: 1.6rem 2rem 3rem !important; max-width: 1240px !important; }

/* ── Sidebar ──────────────────────────────── */
[data-testid="stSidebar"] {
    background: linear-gradient(175deg, #0f2460 0%, #1a3a8a 60%, #1e40af 100%) !important;
    border-right: none !important;
}
[data-testid="stSidebar"] * { color: #bfdbfe !important; }
.sb-brand {
    padding: 26px 22px 20px;
    border-bottom: 1px solid rgba(255,255,255,0.1);
    margin-bottom: 6px;
}
.sb-brand-name {
    font-size: 23px; font-weight: 800; color: #ffffff !important; letter-spacing: -0.5px;
}
.sb-brand-tag {
    display: block; font-size: 10px; letter-spacing: 2px; text-transform: uppercase;
    color: rgba(191,219,254,0.55) !important; margin-top: 4px;
}
.sb-section {
    display: block; font-size: 9.5px; font-weight: 700; letter-spacing: 2px;
    text-transform: uppercase; color: rgba(148,163,184,0.45) !important;
    padding: 16px 22px 6px;
}
[data-testid="stSidebar"] .stRadio > div { gap: 2px !important; }
[data-testid="stSidebar"] .stRadio label {
    padding: 10px 14px !important; border-radius: 9px !important;
    color: #93c5fd !important; font-size: 13.5px !important; font-weight: 500 !important;
    transition: all 0.15s ease !important; margin: 1px 10px !important;
    border: 1px solid transparent !important; cursor: pointer !important;
}
[data-testid="stSidebar"] .stRadio label:hover {
    background: rgba(255,255,255,0.08) !important; color: #fff !important;
}
.sb-footer {
    font-size: 11px; color: rgba(147,197,253,0.35) !important;
    text-align: center; padding: 14px 16px 8px;
    border-top: 1px solid rgba(255,255,255,0.07); margin-top: 12px;
    line-height: 1.6;
}

/* ── Hero Banner ───────────────────────────── */
.hero {
    background: linear-gradient(130deg, #0f2460 0%, #1d4ed8 55%, #3b82f6 100%);
    border-radius: 18px; padding: 32px 40px; margin-bottom: 24px;
    position: relative; overflow: hidden;
    box-shadow: 0 10px 40px rgba(15,36,96,0.35);
}
.hero::before {
    content:''; position:absolute; top:-60px; right:-40px;
    width:230px; height:230px; border-radius:50%;
    background:rgba(255,255,255,0.05);
}
.hero::after {
    content:''; position:absolute; bottom:-80px; right:100px;
    width:280px; height:280px; border-radius:50%;
    background:rgba(255,255,255,0.04);
}
.hero-badge {
    display:inline-flex; align-items:center; gap:5px;
    background:rgba(255,255,255,0.14); border:1px solid rgba(255,255,255,0.22);
    color:#fff !important; padding:4px 13px; border-radius:20px;
    font-size:11px; font-weight:600; letter-spacing:1px; text-transform:uppercase;
    margin-bottom:12px;
}
.hero-title { font-size:28px; font-weight:800; color:#fff; margin:0 0 6px; letter-spacing:-0.5px; }
.hero-sub   { font-size:14px; color:rgba(255,255,255,0.68); margin:0; }

/* ── Form as Card ──────────────────────────── */
[data-testid="stForm"] {
    background: #ffffff !important;
    border: 1px solid #e2e8f0 !important;
    border-radius: 16px !important;
    padding: 28px 30px !important;
    box-shadow: 0 2px 12px rgba(15,23,42,0.06) !important;
}
.form-heading {
    font-size: 15px; font-weight: 700; color: #0f172a;
    padding-bottom: 14px; margin-bottom: 18px;
    border-bottom: 2px solid #f1f5f9;
}

/* ── Info Panel Card ───────────────────────── */
.info-card {
    background: #ffffff; border: 1px solid #e2e8f0; border-radius: 16px;
    padding: 24px 26px; box-shadow: 0 2px 10px rgba(15,23,42,0.05);
}
.info-card-title {
    font-size: 14px; font-weight: 700; color: #0f172a;
    border-bottom: 2px solid #f1f5f9; padding-bottom: 12px; margin-bottom: 14px;
}
.ir { display:flex; justify-content:space-between; align-items:center;
      padding:10px 0; border-bottom:1px solid #f8fafc; font-size:13.5px; }
.ir:last-child { border:none; }
.ir-l { color:#64748b; font-weight:500; }
.ir-r { color:#0f172a; font-weight:600; }

/* ── Stat Cards (Dashboard) ─────────────────── */
.stat-card {
    background:#fff; border-radius:15px; padding:22px 24px;
    border:1px solid #e2e8f0; box-shadow:0 1px 4px rgba(0,0,0,0.04);
    transition: transform 0.2s, box-shadow 0.2s;
}
.stat-card:hover { transform:translateY(-2px); box-shadow:0 6px 22px rgba(15,36,96,0.1); }
.sc-icon { width:44px;height:44px;border-radius:10px;display:flex;align-items:center;
           justify-content:center;font-size:20px;margin-bottom:14px; }
.ic-b  { background:linear-gradient(135deg,#dbeafe,#bfdbfe); }
.ic-g  { background:linear-gradient(135deg,#dcfce7,#bbf7d0); }
.ic-v  { background:linear-gradient(135deg,#ede9fe,#ddd6fe); }
.sc-val{ font-size:30px;font-weight:800;color:#0f172a;letter-spacing:-1px; }
.sc-lbl{ font-size:12px;color:#64748b;font-weight:500;margin-top:3px; }
.sc-sub{ font-size:11px;color:#94a3b8;margin-top:8px;padding-top:8px;border-top:1px solid #f1f5f9; }

/* ── Bank Card ──────────────────────────────── */
.bank-card {
    background:linear-gradient(135deg,#0f2460 0%,#1d4ed8 55%,#6366f1 100%);
    border-radius:20px; padding:28px 30px; color:#fff;
    box-shadow:0 14px 44px rgba(15,36,96,0.4);
    position:relative; overflow:hidden; min-height:195px;
}
.bank-card::before {
    content:''; position:absolute; top:-40px; right:-30px;
    width:160px;height:160px; border:30px solid rgba(255,255,255,0.07); border-radius:50%;
}
.bank-card::after {
    content:''; position:absolute; bottom:-65px; right:50px;
    width:200px;height:200px; border:40px solid rgba(255,255,255,0.04); border-radius:50%;
}
.bc-chip { width:40px;height:28px;border-radius:5px;
           background:linear-gradient(135deg,#f59e0b,#d97706);margin-bottom:22px; }
.bc-bal-lbl{ font-size:10px;opacity:.65;letter-spacing:2px;text-transform:uppercase; }
.bc-bal    { font-size:34px;font-weight:800;letter-spacing:-1px;margin-top:2px; }
.bc-no     { font-size:14px;font-weight:600;letter-spacing:3px;margin-top:14px;opacity:.82; }
.bc-foot   { display:flex;justify-content:space-between;margin-top:16px;padding-top:12px;
             border-top:1px solid rgba(255,255,255,0.15);font-size:11px; }
.bc-fl     { opacity:.6;letter-spacing:1px;text-transform:uppercase; }
.bc-fv     { font-size:14px;font-weight:700;margin-top:2px; }

/* ── Created Account Card ──────────────────── */
.created-card {
    background:linear-gradient(135deg,#f0fdf4,#dcfce7);
    border:1px solid #86efac; border-radius:16px; padding:26px 30px; margin-bottom:16px;
}
.created-title { font-size:17px;font-weight:700;color:#14532d;margin-bottom:18px; }
.created-field { margin-bottom:14px; }
.created-lbl   { font-size:10px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;color:#166534; }
.created-val   {
    display:inline-block; font-size:22px;font-weight:800;color:#14532d;letter-spacing:3px;
    background:#fff; border:1px solid #86efac; border-radius:8px;padding:8px 18px;margin-top:5px;
}
.created-note  { font-size:13px;color:#166534;margin-top:12px; }

/* ── Balance Result Card ────────────────────── */
.bal-card {
    background:#fff; border:1px solid #e2e8f0; border-radius:14px;
    padding:20px 24px; display:inline-flex; align-items:center; gap:16px;
    box-shadow:0 2px 10px rgba(0,0,0,0.05); margin-top:4px;
}
.bal-icon { width:48px;height:48px;border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:22px; }
.bal-amount{ font-size:28px;font-weight:800;color:#0f172a;letter-spacing:-1px; }
.bal-label { font-size:12px;color:#64748b;font-weight:500;margin-top:2px; }

/* ── Transactions ───────────────────────────── */
.txn {
    display:flex;justify-content:space-between;align-items:center;
    background:#fff;border:1px solid #f1f5f9;border-radius:12px;
    padding:13px 18px;margin-bottom:7px;
    box-shadow:0 1px 3px rgba(0,0,0,0.03); transition:box-shadow 0.15s;
}
.txn:hover { box-shadow:0 4px 14px rgba(0,0,0,0.07); }
.txn-left { display:flex;align-items:center;gap:13px; }
.txn-dot  { width:38px;height:38px;border-radius:10px;flex-shrink:0;
            display:flex;align-items:center;justify-content:center;font-size:16px; }
.td-cr { background:linear-gradient(135deg,#dcfce7,#bbf7d0); }
.td-db { background:linear-gradient(135deg,#fee2e2,#fecaca); }
.txn-desc  { font-size:14px;font-weight:600;color:#0f172a; }
.txn-date  { font-size:11px;color:#94a3b8;margin-top:2px; }
.txn-cr    { font-size:15px;font-weight:700;color:#16a34a; }
.txn-db    { font-size:15px;font-weight:700;color:#dc2626; }
.txn-bal   { font-size:11px;color:#94a3b8;text-align:right;margin-top:2px; }

/* ── Pills ──────────────────────────────────── */
.pill { display:inline-flex;align-items:center;padding:3px 10px;border-radius:20px;
        font-size:11px;font-weight:700;letter-spacing:.3px; }
.p-g { background:#dcfce7;color:#15803d; }
.p-b { background:#dbeafe;color:#1d4ed8; }
.p-s { background:#f1f5f9;color:#475569; }
.p-o { background:#fff7ed;color:#c2410c; }

/* ── Notice / Warning / Danger ──────────────── */
.notice {
    background:#eff6ff;border:1px solid #bfdbfe;border-radius:12px;
    padding:14px 18px;font-size:13px;color:#1e40af;
    display:flex;gap:10px;align-items:flex-start;margin-top:12px;
}
.warn  { background:#fff7ed;border:1px solid #fed7aa;border-radius:12px;
         padding:14px 18px;font-size:13px;color:#9a3412;margin-top:10px; }
.danger{ background:#fff1f2;border:1px solid #fecdd3;border-radius:12px;
         padding:16px 20px;font-size:13px;color:#9f1239;line-height:1.7;margin-bottom:18px; }

/* ── Quick Action Cards ─────────────────────── */
.qa-card {
    background:#fff;border-radius:14px;padding:20px 14px;
    border:1px solid #e2e8f0;text-align:center;
    box-shadow:0 1px 4px rgba(0,0,0,0.04);transition:all 0.2s;
}
.qa-card:hover {
    transform:translateY(-3px);border-color:#93c5fd;
    box-shadow:0 8px 24px rgba(15,36,96,0.12);
}
.qa-ic  { font-size:28px;margin-bottom:8px; }
.qa-ttl { font-size:14px;font-weight:700;color:#0f172a; }
.qa-sub { font-size:11px;color:#94a3b8;margin-top:3px; }

/* ── Step indicator ─────────────────────────── */
.steps { display:flex;align-items:center;margin-bottom:22px; }
.step  { display:flex;align-items:center;gap:8px;font-size:13px;font-weight:600; }
.step-n{ width:28px;height:28px;border-radius:50%;display:flex;align-items:center;
         justify-content:center;font-size:12px;font-weight:700; }
.s-a .step-n { background:#1d4ed8;color:#fff; }
.s-d .step-n { background:#16a34a;color:#fff; }
.s-w .step-n { background:#e2e8f0;color:#94a3b8; }
.s-a .step-lbl { color:#1d4ed8; }
.s-d .step-lbl { color:#16a34a; }
.s-w .step-lbl { color:#94a3b8; }
.step-line { flex:1;height:2px;background:#e2e8f0;margin:0 10px; }
.step-line-d { background:#16a34a; }

/* ── Inputs ─────────────────────────────────── */
.stTextInput label,.stNumberInput label,.stCheckbox label {
    font-size:13px !important;font-weight:600 !important;color:#374151 !important;
}
.stTextInput input,.stNumberInput input {
    border:1.5px solid #e2e8f0 !important;border-radius:9px !important;
    background:#f8fafc !important;color:#0f172a !important;
    font-size:14px !important;padding:10px 13px !important;transition:all 0.2s !important;
}
.stTextInput input:focus,.stNumberInput input:focus {
    border-color:#3b82f6 !important;background:#fff !important;
    box-shadow:0 0 0 3px rgba(59,130,246,0.12) !important;
}
.stTextInput input::placeholder { color:#94a3b8 !important; }

/* ── Buttons ─────────────────────────────────── */
.stButton > button {
    border-radius:9px !important;font-weight:700 !important;
    font-size:14px !important;height:46px !important;
    transition:all 0.2s !important;letter-spacing:0.1px !important;
}
.stButton > button[kind="primary"] {
    background:linear-gradient(135deg,#1e3a8a,#2563eb) !important;
    color:#fff !important;border:none !important;
    box-shadow:0 4px 14px rgba(37,99,235,0.35) !important;
}
.stButton > button[kind="primary"]:hover {
    transform:translateY(-1px) !important;
    box-shadow:0 7px 22px rgba(37,99,235,0.45) !important;
}
.stButton > button:not([kind="primary"]) {
    background:#fff !important;color:#1d4ed8 !important;
    border:1.5px solid #93c5fd !important;
}
.stButton > button:not([kind="primary"]):hover {
    background:#eff6ff !important;border-color:#3b82f6 !important;
}

/* ── Alerts ──────────────────────────────────── */
.stAlert > div { border-radius:12px !important;font-size:14px !important; }

/* ── Metric ──────────────────────────────────── */
[data-testid="stMetric"] {
    background:#fff;border-radius:12px;padding:16px 20px;border:1px solid #e2e8f0;
}
[data-testid="stMetricValue"] { color:#0f172a !important;font-weight:800 !important; }
[data-testid="stMetricLabel"] { color:#64748b !important;font-size:13px !important; }

hr { border:none;border-top:1px solid #e2e8f0 !important;margin:16px 0 !important; }
::-webkit-scrollbar { width:6px; }
::-webkit-scrollbar-thumb { background:#cbd5e1;border-radius:3px; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────
DATABASE       = Path(__file__).parent / "data.json"
MAX_DEPOSIT    = 100_000
MIN_DEPOSIT    = 1
MAX_WITHDRAWAL = 100_000


# ═════════════════════════════════════════
#  Bank Core
# ═════════════════════════════════════════
class Bank:
    @staticmethod
    def _load():
        try:
            if DATABASE.exists():
                with open(DATABASE, encoding="utf-8") as f:
                    return json.load(f)
        except Exception:
            pass
        return []

    @staticmethod
    def _save(data):
        DATABASE.parent.mkdir(parents=True, exist_ok=True)
        with open(DATABASE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    @staticmethod
    def _gen_acno():
        return "NEO" + "".join(random.choices(string.digits, k=9))

    @staticmethod
    def _ts():
        return datetime.datetime.now().strftime("%d %b %Y, %I:%M %p")

    @staticmethod
    def _find(data, acno, pin):
        for a in data:
            if a["accountNo"] == acno and a["pin"] == pin:
                return a
        return None

    @classmethod
    def create_account(cls, name, age, email, pin):
        name, email = name.strip(), email.strip().lower()
        if not name:
            return False, "Full name is required.", {}
        if age < 18:
            return False, "Minimum age is 18 years.", {}
        if not (1000 <= pin <= 9999):
            return False, "PIN must be exactly 4 digits (1000–9999).", {}
        if "@" not in email or "." not in email.split("@")[-1]:
            return False, "Enter a valid email address.", {}
        data = cls._load()
        if any(a["email"] == email for a in data):
            return False, "An account with this email already exists.", {}
        acno = cls._gen_acno()
        while any(a["accountNo"] == acno for a in data):
            acno = cls._gen_acno()
        info = {
            "name": name.title(), "age": age, "email": email,
            "pin": pin, "accountNo": acno,
            "balance": 0.0, "created_at": cls._ts(), "transactions": [],
        }
        data.append(info)
        cls._save(data)
        return True, "Account created successfully!", info

    @classmethod
    def deposit(cls, acno, pin, amount):
        data = cls._load()
        acct = cls._find(data, acno, pin)
        if not acct:
            return False, "Invalid account number or PIN.", 0.0
        if not (MIN_DEPOSIT <= amount <= MAX_DEPOSIT):
            return False, f"Amount must be ₹{MIN_DEPOSIT:,} – ₹{MAX_DEPOSIT:,}.", 0.0
        acct["balance"] = round(acct["balance"] + amount, 2)
        acct.setdefault("transactions", []).append({
            "type": "credit", "amount": amount, "date": cls._ts(),
            "description": "Cash Deposit", "balance_after": acct["balance"],
        })
        cls._save(data)
        return True, f"₹{amount:,.2f} deposited successfully.", acct["balance"]

    @classmethod
    def withdraw(cls, acno, pin, amount):
        data = cls._load()
        acct = cls._find(data, acno, pin)
        if not acct:
            return False, "Invalid account number or PIN.", 0.0
        if amount <= 0:
            return False, "Amount must be greater than ₹0.", 0.0
        if amount > MAX_WITHDRAWAL:
            return False, f"Maximum per transaction: ₹{MAX_WITHDRAWAL:,}.", 0.0
        if acct["balance"] < amount:
            return False, f"Insufficient balance. Available: ₹{acct['balance']:,.2f}", 0.0
        acct["balance"] = round(acct["balance"] - amount, 2)
        acct.setdefault("transactions", []).append({
            "type": "debit", "amount": amount, "date": cls._ts(),
            "description": "Cash Withdrawal", "balance_after": acct["balance"],
        })
        cls._save(data)
        return True, f"₹{amount:,.2f} withdrawn successfully.", acct["balance"]

    @classmethod
    def get_account(cls, acno, pin):
        acct = cls._find(cls._load(), acno, pin)
        if not acct:
            return False, "Invalid account number or PIN.", {}
        return True, "OK", dict(acct)

    @classmethod
    def update_account(cls, acno, pin, new_name, new_email, new_pin):
        data = cls._load()
        acct = cls._find(data, acno, pin)
        if not acct:
            return False, "Invalid account number or PIN."
        if new_name.strip():
            acct["name"] = new_name.strip().title()
        if new_email.strip():
            em = new_email.strip().lower()
            if "@" not in em or "." not in em.split("@")[-1]:
                return False, "Invalid email address."
            if any(a["email"] == em and a["accountNo"] != acno for a in data):
                return False, "Email already used by another account."
            acct["email"] = em
        if new_pin is not None:
            if not (1000 <= new_pin <= 9999):
                return False, "New PIN must be 4 digits."
            acct["pin"] = new_pin
        cls._save(data)
        return True, "Profile updated successfully!"

    @classmethod
    def delete_account(cls, acno, pin):
        data = cls._load()
        acct = cls._find(data, acno, pin)
        if not acct:
            return False, "Invalid account number or PIN."
        data.remove(acct)
        cls._save(data)
        return True, "Account closed permanently."

    @classmethod
    def stats(cls):
        data = cls._load()
        return {
            "accounts": len(data),
            "balance":  sum(a.get("balance", 0) for a in data),
            "transactions": sum(len(a.get("transactions", [])) for a in data),
        }


# ═════════════════════════════════════════
#  UI helpers
# ═════════════════════════════════════════
def sidebar_nav():
    with st.sidebar:
        st.markdown("""
        <div class="sb-brand">
            <div class="sb-brand-name">🏦 NeoBank</div>
            <span class="sb-brand-tag">Secure · Modern · Trusted</span>
        </div>""", unsafe_allow_html=True)
        st.markdown('<span class="sb-section">Main Menu</span>', unsafe_allow_html=True)

        pages = {
            "🏠  Dashboard":        "Dashboard",
            "➕  Open Account":     "Open Account",
            "💳  Deposit Funds":    "Deposit",
            "💸  Withdraw Funds":   "Withdraw",
            "👤  Account Details":  "Account Details",
            "✏️   Update Profile":   "Update Profile",
            "🗑️   Close Account":    "Delete Account",
        }
        choice = st.radio("nav", list(pages.keys()), label_visibility="collapsed")
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""<div class="sb-footer">NeoBank v2.0 · © 2026<br>
        All data is encrypted & secured.</div>""", unsafe_allow_html=True)
    return pages[choice]


def hero(title, subtitle, badge=""):
    b = f'<div class="hero-badge">🔒 {badge}</div>' if badge else ""
    st.markdown(f"""
    <div class="hero">{b}
        <div class="hero-title">{title}</div>
        <p class="hero-sub">{subtitle}</p>
    </div>""", unsafe_allow_html=True)


def bank_card_html(acct):
    fmt = " ".join(acct["accountNo"][i:i+4] for i in range(0, len(acct["accountNo"]), 4))
    st.markdown(f"""
    <div class="bank-card">
        <div class="bc-chip"></div>
        <div class="bc-bal-lbl">Available Balance</div>
        <div class="bc-bal">₹{acct['balance']:,.2f}</div>
        <div class="bc-no">{fmt}</div>
        <div class="bc-foot">
            <div><div class="bc-fl">Account Holder</div>
                 <div class="bc-fv">{acct['name']}</div></div>
            <div style="text-align:right;">
                <div class="bc-fl">Member Since</div>
                <div class="bc-fv">{acct.get('created_at','')[:11]}</div>
            </div>
        </div>
    </div>""", unsafe_allow_html=True)


def txn_row(txn):
    cr = txn["type"] == "credit"
    st.markdown(f"""
    <div class="txn">
        <div class="txn-left">
            <div class="txn-dot {'td-cr' if cr else 'td-db'}">{'⬆️' if cr else '⬇️'}</div>
            <div>
                <div class="txn-desc">{txn.get('description','Transaction')}</div>
                <div class="txn-date">🕐 {txn['date']}</div>
            </div>
        </div>
        <div style="text-align:right;">
            <div class="{'txn-cr' if cr else 'txn-db'}">{'+' if cr else '−'} ₹{txn['amount']:,.2f}</div>
            <div class="txn-bal">Bal: ₹{txn.get('balance_after',0):,.2f}</div>
        </div>
    </div>""", unsafe_allow_html=True)


def ir(label, value, pill=""):
    v = f'<span class="pill {pill}">{value}</span>' if pill else f'<span class="ir-r">{value}</span>'
    st.markdown(f'<div class="ir"><span class="ir-l">{label}</span>{v}</div>',
                unsafe_allow_html=True)


def show_flash(key):
    """Display a stored flash result then clear it."""
    r = st.session_state.pop(key, None)
    if not r:
        return
    if r["ok"]:
        st.success(f"✅ {r['msg']}")
    else:
        st.error(f"❌ {r['msg']}")


def bal_result(bal, label, color="#0f172a", icon_cls="ic-b"):
    st.markdown(f"""
    <div class="bal-card">
        <div class="bal-icon {icon_cls}">💰</div>
        <div>
            <div class="bal-amount" style="color:{color};">₹{bal:,.2f}</div>
            <div class="bal-label">{label}</div>
        </div>
    </div>""", unsafe_allow_html=True)


# ═════════════════════════════════════════
#  Pages
# ═════════════════════════════════════════

# ── Dashboard ─────────────────────────────
def page_dashboard():
    hero("Welcome to NeoBank",
         "Your complete digital banking dashboard — secure, fast, and reliable.",
         "Secured Banking")

    s = Bank.stats()
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"""<div class="stat-card">
            <div class="sc-icon ic-b">👥</div>
            <div class="sc-val">{s['accounts']:,}</div>
            <div class="sc-lbl">Total Accounts</div>
            <div class="sc-sub">Active & verified customers</div>
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown(f"""<div class="stat-card">
            <div class="sc-icon ic-g">💰</div>
            <div class="sc-val">₹{s['balance']:,.0f}</div>
            <div class="sc-lbl">Total Balance Held</div>
            <div class="sc-sub">Across all accounts</div>
        </div>""", unsafe_allow_html=True)
    with c3:
        st.markdown(f"""<div class="stat-card">
            <div class="sc-icon ic-v">🔄</div>
            <div class="sc-val">{s['transactions']:,}</div>
            <div class="sc-lbl">Total Transactions</div>
            <div class="sc-sub">Deposits & withdrawals</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### ⚡ Quick Actions")
    q1, q2, q3, q4 = st.columns(4)
    for col, icon, title, sub, target in [
        (q1, "➕", "Open Account",    "Start banking today",    "Open Account"),
        (q2, "💳", "Deposit Funds",   "Add money instantly",    "Deposit"),
        (q3, "💸", "Withdraw Funds",  "Access your funds",      "Withdraw"),
        (q4, "👤", "Account Details", "Balance & history",      "Account Details"),
    ]:
        with col:
            st.markdown(f"""<div class="qa-card">
                <div class="qa-ic">{icon}</div>
                <div class="qa-ttl">{title}</div>
                <div class="qa-sub">{sub}</div>
            </div>""", unsafe_allow_html=True)
            if st.button(title, key=f"qa_{target}", use_container_width=True):
                st.session_state["_nav"] = target
                st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""<div class="notice"><span style="font-size:18px;flex-shrink:0;">🔐</span>
    <div><strong>Security Reminder:</strong> Never share your PIN with anyone.
    NeoBank staff will never ask for your PIN via phone, email, or chat.</div>
    </div>""", unsafe_allow_html=True)


# ── Open Account ───────────────────────────
def page_open_account():
    hero("Open a New Account",
         "Free savings account — instant activation, zero hidden fees.",
         "Free · No Hidden Charges")

    # ① show flash result FIRST
    r = st.session_state.pop("create_flash", None)
    if r:
        if r["ok"]:
            info = r["info"]
            st.balloons()
            st.markdown(f"""
            <div class="created-card">
                <div class="created-title">🎉 Account Created Successfully!</div>
                <div class="created-field">
                    <div class="created-lbl">Account Number</div>
                    <div class="created-val">{info['accountNo']}</div>
                </div>
                <div class="created-field" style="margin-top:14px;">
                    <div class="created-lbl">Your PIN</div>
                    <div class="created-val">{info['pin']}</div>
                </div>
                <div class="created-note">
                    ⚠️ Save these details — you need them for every future transaction.
                </div>
            </div>""", unsafe_allow_html=True)
        else:
            st.error(f"❌ {r['msg']}")

    # ② layout
    left, right = st.columns([3, 2], gap="large")
    with left:
        with st.form("frm_create"):
            st.markdown('<div class="form-heading">📋 Personal Information</div>',
                        unsafe_allow_html=True)
            c1, c2 = st.columns(2)
            with c1:
                name  = st.text_input("Full Name *", placeholder="e.g. Swapnil Patil")
                age   = st.number_input("Age *", min_value=1, max_value=120, value=18, step=1)
            with c2:
                email = st.text_input("Email Address *", placeholder="e.g. swapnil@email.com")
                pin   = st.number_input("4-Digit PIN *", min_value=1000, max_value=9999,
                                        step=1, help="A 4-digit number you'll remember.")
            st.markdown("<br>", unsafe_allow_html=True)
            sub = st.form_submit_button("🚀  Create My Account",
                                        use_container_width=True, type="primary")

    with right:
        st.markdown("""<div class="info-card">
            <div class="info-card-title">📌 Eligibility & Terms</div>""",
            unsafe_allow_html=True)
        ir("Minimum Age",          "18+ years",      "pill p-b")
        ir("Account Type",         "Savings",         "pill p-s")
        ir("Joining Fee",          "₹0 Free",         "pill p-g")
        ir("PIN Format",           "4 digits",        "pill p-s")
        ir("Max Deposit / Txn",    "₹1,00,000",       "pill p-s")
        ir("Max Withdrawal / Txn", "₹1,00,000",       "pill p-s")
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("""<div class="notice"><span>🛡️</span>
        <div>Your data is encrypted and never shared with third parties.</div>
        </div>""", unsafe_allow_html=True)

    # ③ process AFTER layout → store flash → rerun to show at top
    if sub:
        ok, msg, info = Bank.create_account(name, int(age), email, int(pin))
        st.session_state["create_flash"] = {"ok": ok, "msg": msg, "info": info}
        st.rerun()


# ── Deposit ────────────────────────────────
def page_deposit():
    hero("Deposit Funds",
         "Add money to your NeoBank account — credited instantly.",
         "Instant Credit")

    # ① flash
    r = st.session_state.pop("dep_flash", None)
    if r:
        if r["ok"]:
            st.success(f"✅ {r['msg']}")
            bal_result(r["bal"], "Updated Account Balance", "#16a34a", "ic-g")
        else:
            st.error(f"❌ {r['msg']}")

    st.markdown("<br>", unsafe_allow_html=True)

    # ② layout
    left, right = st.columns([3, 2], gap="large")
    with left:
        with st.form("frm_dep"):
            st.markdown('<div class="form-heading">💳 Deposit Details</div>',
                        unsafe_allow_html=True)
            c1, c2 = st.columns(2)
            with c1:
                acno = st.text_input("Account Number", placeholder="NEO123456789")
            with c2:
                pin  = st.number_input("PIN", min_value=1000, max_value=9999, step=1)
            amount = st.number_input(
                f"Amount to Deposit (₹)  —  max ₹{MAX_DEPOSIT:,}",
                min_value=1.0, max_value=float(MAX_DEPOSIT), step=100.0, value=1000.0
            )
            st.markdown("<br>", unsafe_allow_html=True)
            sub = st.form_submit_button("💳  Deposit Now",
                                        use_container_width=True, type="primary")

    with right:
        st.markdown("""<div class="info-card">
            <div class="info-card-title">📊 Deposit Policy</div>""",
            unsafe_allow_html=True)
        ir("Minimum Deposit",         f"₹{MIN_DEPOSIT:,}")
        ir("Maximum / Transaction",   f"₹{MAX_DEPOSIT:,}")
        ir("Processing Time",         "Instant",   "pill p-g")
        ir("Transaction Fee",         "₹0 Free",   "pill p-g")
        st.markdown("</div>", unsafe_allow_html=True)

    # ③ process
    if sub:
        ok, msg, bal = Bank.deposit(acno.strip(), int(pin), float(amount))
        st.session_state["dep_flash"] = {"ok": ok, "msg": msg, "bal": bal}
        st.rerun()


# ── Withdraw ───────────────────────────────
def page_withdraw():
    hero("Withdraw Funds",
         "Access your money anytime — processed instantly, zero fees.",
         "Instant Processing")

    # ① flash
    r = st.session_state.pop("wd_flash", None)
    if r:
        if r["ok"]:
            st.success(f"✅ {r['msg']}")
            bal_result(r["bal"], "Remaining Account Balance", "#1d4ed8", "ic-b")
        else:
            st.error(f"❌ {r['msg']}")

    st.markdown("<br>", unsafe_allow_html=True)

    # ② layout
    left, right = st.columns([3, 2], gap="large")
    with left:
        with st.form("frm_wd"):
            st.markdown('<div class="form-heading">💸 Withdrawal Details</div>',
                        unsafe_allow_html=True)
            c1, c2 = st.columns(2)
            with c1:
                acno = st.text_input("Account Number", placeholder="NEO123456789")
            with c2:
                pin  = st.number_input("PIN", min_value=1000, max_value=9999, step=1)
            amount = st.number_input(
                f"Amount to Withdraw (₹)  —  max ₹{MAX_WITHDRAWAL:,}",
                min_value=1.0, max_value=float(MAX_WITHDRAWAL), step=100.0, value=500.0
            )
            st.markdown("<br>", unsafe_allow_html=True)
            sub = st.form_submit_button("💸  Withdraw Now",
                                        use_container_width=True, type="primary")

    with right:
        st.markdown("""<div class="info-card">
            <div class="info-card-title">📊 Withdrawal Policy</div>""",
            unsafe_allow_html=True)
        ir("Minimum Amount",          "₹1")
        ir("Maximum / Transaction",   f"₹{MAX_WITHDRAWAL:,}")
        ir("Processing Time",         "Instant",   "pill p-g")
        ir("Transaction Fee",         "₹0 Free",   "pill p-g")
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("""<div class="warn">
        ⚠️ Ensure sufficient balance. Withdrawals cannot be reversed once processed.
        </div>""", unsafe_allow_html=True)

    # ③ process
    if sub:
        ok, msg, bal = Bank.withdraw(acno.strip(), int(pin), float(amount))
        st.session_state["wd_flash"] = {"ok": ok, "msg": msg, "bal": bal}
        st.rerun()


# ── Account Details ────────────────────────
def page_account_details():
    hero("Account Details",
         "View your balance, profile, and complete transaction history.",
         "Full Overview")

    # ① flash error (auth failed)
    r = st.session_state.pop("det_flash", None)
    if r and not r["ok"]:
        st.error(f"❌ {r['msg']}")

    # ② auth form
    with st.form("frm_det"):
        st.markdown('<div class="form-heading">🔐 Verify Identity</div>',
                    unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            acno = st.text_input("Account Number", placeholder="NEO123456789")
        with c2:
            pin  = st.number_input("PIN", min_value=1000, max_value=9999, step=1)
        st.markdown("<br>", unsafe_allow_html=True)
        sub = st.form_submit_button("🔍  Fetch My Account",
                                    use_container_width=True, type="primary")

    # ③ process auth
    if sub:
        ok, msg, acct = Bank.get_account(acno.strip(), int(pin))
        if ok:
            st.session_state["det_acct"] = acct
        else:
            st.session_state.pop("det_acct", None)
            st.session_state["det_flash"] = {"ok": False, "msg": msg}
        st.rerun()

    # ④ display account if authenticated
    acct = st.session_state.get("det_acct")
    if not acct:
        return

    st.markdown("<br>", unsafe_allow_html=True)
    left, right = st.columns([3, 2], gap="large")
    with left:
        bank_card_html(acct)
    with right:
        st.markdown("""<div class="info-card">
            <div class="info-card-title">👤 Profile Details</div>""",
            unsafe_allow_html=True)
        ir("Full Name",    acct["name"])
        ir("Email",        acct["email"])
        ir("Age",          str(acct["age"]))
        ir("Joined",       acct.get("created_at", "—")[:18])
        ir("Status",       "✅ Active",   "pill p-g")
        ir("Account Type", "Savings",     "pill p-b")
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    txns = acct.get("transactions", [])
    h1, h2 = st.columns([5, 1])
    with h1:
        st.markdown("### 📋 Transaction History")
    with h2:
        st.markdown(f'<div style="padding-top:14px;text-align:right;">'
                    f'<span class="pill p-s">{len(txns)} records</span></div>',
                    unsafe_allow_html=True)

    if not txns:
        st.markdown("""<div class="notice" style="flex-direction:column;text-align:center;padding:32px;">
            <div style="font-size:38px;margin-bottom:10px;">🏦</div>
            <strong>No transactions yet.</strong><br>Start by depositing money.
        </div>""", unsafe_allow_html=True)
    else:
        for t in reversed(txns[-25:]):
            txn_row(t)
        if len(txns) > 25:
            st.caption(f"Showing latest 25 of {len(txns)} transactions.")


# ── Update Profile ─────────────────────────
def page_update_profile():
    hero("Update Profile",
         "Securely update your name, email, or PIN.",
         "Manage Profile")

    verified = st.session_state.get("upd_ok", False)

    st.markdown(f"""
    <div class="steps">
        <div class="step {'s-d' if verified else 's-a'}">
            <div class="step-n">{'✓' if verified else '1'}</div>
            <span class="step-lbl">Verify Identity</span>
        </div>
        <div class="step-line {'step-line-d' if verified else ''}"></div>
        <div class="step {'s-a' if verified else 's-w'}">
            <div class="step-n">2</div>
            <span class="step-lbl">Edit Details</span>
        </div>
        <div class="step-line"></div>
        <div class="step s-w">
            <div class="step-n">3</div>
            <span class="step-lbl">Save Changes</span>
        </div>
    </div>""", unsafe_allow_html=True)

    # flash from save
    r = st.session_state.pop("upd_flash", None)
    if r:
        if r["ok"]:
            st.success(f"✅ {r['msg']}")
        else:
            st.error(f"❌ {r['msg']}")

    if not verified:
        with st.form("frm_upd_v"):
            st.markdown('<div class="form-heading">🔐 Step 1 — Verify Your Identity</div>',
                        unsafe_allow_html=True)
            c1, c2 = st.columns(2)
            with c1:
                acno = st.text_input("Account Number", placeholder="NEO123456789")
            with c2:
                pin  = st.number_input("Current PIN", min_value=1000, max_value=9999, step=1)
            st.markdown("<br>", unsafe_allow_html=True)
            vsub = st.form_submit_button("🔑  Verify Identity",
                                         use_container_width=True, type="primary")
        if vsub:
            ok, msg, acct = Bank.get_account(acno.strip(), int(pin))
            if ok:
                st.session_state.update({"upd_ok": True, "upd_acno": acno.strip(),
                                          "upd_pin": int(pin), "upd_acct": acct})
            else:
                st.session_state["upd_flash"] = {"ok": False, "msg": msg}
            st.rerun()
        return

    acct = st.session_state["upd_acct"]
    st.info(f"✅ Verified — **{acct['name']}** | {acct['email']}")

    with st.form("frm_upd_e"):
        st.markdown('<div class="form-heading">✏️ Step 2 — Update Your Details</div>',
                    unsafe_allow_html=True)
        st.caption("Leave blank to keep the existing value.")
        c1, c2 = st.columns(2)
        with c1:
            new_name  = st.text_input("New Full Name",     placeholder=acct["name"])
            new_email = st.text_input("New Email Address", placeholder=acct["email"])
        with c2:
            change_pin = st.checkbox("Change my PIN")
            new_pin    = None
            if change_pin:
                new_pin = st.number_input("New PIN (4 digits)",
                                          min_value=1000, max_value=9999, step=1)
        st.markdown("<br>", unsafe_allow_html=True)
        ssub = st.form_submit_button("💾  Save Changes",
                                     use_container_width=True, type="primary")

    if ssub:
        ok, msg = Bank.update_account(
            st.session_state["upd_acno"], st.session_state["upd_pin"],
            new_name, new_email,
            int(new_pin) if (change_pin and new_pin) else None,
        )
        st.session_state["upd_flash"] = {"ok": ok, "msg": msg}
        if ok:
            for k in ("upd_ok", "upd_acno", "upd_pin", "upd_acct"):
                st.session_state.pop(k, None)
        st.rerun()

    if st.button("↩️  Start Over", key="upd_reset"):
        for k in ("upd_ok", "upd_acno", "upd_pin", "upd_acct", "upd_flash"):
            st.session_state.pop(k, None)
        st.rerun()


# ── Delete Account ─────────────────────────
def page_delete_account():
    hero("Close Account",
         "Permanently delete your NeoBank account and all associated data.",
         "Irreversible Action")

    st.markdown("""<div class="danger">
        <strong>⚠️ Warning — This action is permanent and cannot be undone.</strong><br>
        • All personal information will be permanently deleted<br>
        • Complete transaction history will be erased<br>
        • Any remaining balance will be forfeited
    </div>""", unsafe_allow_html=True)

    # flash
    r = st.session_state.pop("del_flash", None)
    if r:
        if r["ok"]:
            st.success(f"✅ {r['msg']} Your account has been permanently closed.")
        else:
            st.error(f"❌ {r['msg']}")

    with st.form("frm_del"):
        st.markdown('<div class="form-heading">🔐 Confirm Account Closure</div>',
                    unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            acno = st.text_input("Account Number", placeholder="NEO123456789")
        with c2:
            pin  = st.number_input("PIN", min_value=1000, max_value=9999, step=1)
        st.markdown("<br>", unsafe_allow_html=True)
        confirm = st.checkbox("I fully understand this is permanent and irreversible.")
        st.markdown("<br>", unsafe_allow_html=True)
        sub = st.form_submit_button("🗑️  Permanently Close Account", use_container_width=True)

    if sub:
        if not confirm:
            st.session_state["del_flash"] = {"ok": False, "msg": "Please tick the confirmation checkbox."}
        else:
            ok, msg = Bank.delete_account(acno.strip(), int(pin))
            st.session_state["del_flash"] = {"ok": ok, "msg": msg}
            if ok:
                st.session_state.pop("det_acct", None)
        st.rerun()


# ═════════════════════════════════════════
#  Router
# ═════════════════════════════════════════
def main():
    page = sidebar_nav()

    if "_nav" in st.session_state:
        page = st.session_state.pop("_nav")

    # Clear per-page state on navigation change
    prev = st.session_state.get("_page")
    if prev != page:
        for k in ("create_flash", "dep_flash", "wd_flash",
                  "det_acct", "det_flash",
                  "upd_ok", "upd_acno", "upd_pin", "upd_acct", "upd_flash",
                  "del_flash"):
            st.session_state.pop(k, None)
        st.session_state["_page"] = page

    {
        "Dashboard":       page_dashboard,
        "Open Account":    page_open_account,
        "Deposit":         page_deposit,
        "Withdraw":        page_withdraw,
        "Account Details": page_account_details,
        "Update Profile":  page_update_profile,
        "Delete Account":  page_delete_account,
    }.get(page, page_dashboard)()


if __name__ == "__main__":
    main()
