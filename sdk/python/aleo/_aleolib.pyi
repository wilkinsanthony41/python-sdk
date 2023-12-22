from __future__ import annotations
from typing import List, Mapping, Optional, Tuple


class Account:
    @staticmethod
    def from_private_key(private_key: PrivateKey) -> Account: ...
    def private_key(self) -> PrivateKey: ...
    def view_key(self) -> ViewKey: ...
    def address(self) -> Address: ...
    def sign(self, message: bytes) -> Signature: ...
    def verify(self, signature: Signature, message: bytes) -> bool: ...
    def decrypt(self, record_ciphertext: RecordCiphertext) -> RecordPlaintext: ...
    def is_owner(self, record_ciphertext: RecordCiphertext) -> bool: ...


class Address:
    @staticmethod
    def from_string(s: str) -> Address: ...


class Authorization:
    @staticmethod
    def from_json(json: str) -> Authorization: ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_bytes(bytes: bytes) -> Authorization: ...
    def bytes(self) -> bytes: ...


class Boolean:
    def __new__(cls, b: bool) -> Boolean: ...


class Ciphertext:
    @staticmethod
    def from_string(s: str) -> Ciphertext: ...
    def decrypt(self, view_key: ViewKey, nonce: Group) -> Plaintext: ...
    def decrypt_symmetric(self, plaintext_view_key: Field) -> Plaintext: ...


class Credits:
    def __new__(cls, value: float) -> Credits: ...
    def micro(self) -> MicroCredits: ...


class CoinbasePuzzle:
    @staticmethod
    def load() -> CoinbasePuzzle: ...
    def verifying_key(self) -> CoinbaseVerifyingKey: ...


class CoinbaseVerifyingKey:
    pass


class ComputeKey:
    def address(self) -> Address: ...
    def pk_sig(self) -> Group: ...
    def pr_sig(self) -> Group: ...
    def sk_prf(self) -> Scalar: ...


class EpochChallenge:
    @staticmethod
    def from_json(json: str) -> EpochChallenge: ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_bytes(bytes: bytes) -> EpochChallenge: ...
    def bytes(self) -> bytes: ...


class Execution:
    def execution_id(self) -> Field: ...
    @staticmethod
    def from_json(json: str) -> Execution: ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_bytes(bytes: bytes) -> Execution: ...
    def bytes(self) -> bytes: ...


class Fee:
    def is_fee_private(self) -> bool: ...
    def is_fee_public(self) -> bool: ...
    def payer(self) -> Optional[Address]: ...
    def transition(self) -> Transition: ...
    @staticmethod
    def from_json(json: str) -> Fee: ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_bytes(bytes: bytes) -> Fee: ...
    def bytes(self) -> bytes: ...


class Field:
    @staticmethod
    def random() -> Field: ...
    @staticmethod
    def from_string(s: str) -> Field: ...
    @staticmethod
    def domain_separator(domain: str) -> Field: ...
    @staticmethod
    def from_u128(u128: int) -> Field: ...
    @staticmethod
    def zero() -> Field: ...
    def __mul__(self, other: Field) -> Field: ...
    def __truediv__(self, other: Field) -> Field: ...


class Group:
    @staticmethod
    def from_string(s: str) -> Group: ...
    @staticmethod
    def zero() -> Group: ...


class Identifier:
    @staticmethod
    def from_string(s: str) -> Identifier: ...


class I8:
    def __new__(cls, value: int) -> I8: ...
    @staticmethod
    def zero() -> I8: ...
    def __int__(self) -> int: ...


class I16:
    def __new__(cls, value: int) -> I16: ...
    @staticmethod
    def zero() -> I16: ...
    def __int__(self) -> int: ...


class I32:
    def __new__(cls, value: int) -> I32: ...
    @staticmethod
    def zero() -> I32: ...
    def __int__(self) -> int: ...


class I64:
    def __new__(cls, value: int) -> I64: ...
    @staticmethod
    def zero() -> I64: ...
    def __int__(self) -> int: ...


class I128:
    def __new__(cls, value: int) -> I128: ...
    @staticmethod
    def zero() -> I128: ...
    def __int__(self) -> int: ...


class Literal:
    @staticmethod
    def parse(s: str) -> Literal: ...
    @staticmethod
    def from_address(address: Address) -> Literal: ...
    @staticmethod
    def from_field(field: Field) -> Literal: ...
    @staticmethod
    def from_group(group: Group) -> Literal: ...
    @staticmethod
    def from_scalar(scalar: Scalar) -> Literal: ...
    @staticmethod
    def from_signature(signature: Signature) -> Literal: ...
    @staticmethod
    def from_boolean(boolean: Boolean) -> Literal: ...
    @staticmethod
    def from_i8(value: I8) -> Literal: ...
    @staticmethod
    def from_i16(value: I16) -> Literal: ...
    @staticmethod
    def from_i32(value: I32) -> Literal: ...
    @staticmethod
    def from_i64(value: I64) -> Literal: ...
    @staticmethod
    def from_i128(value: I128) -> Literal: ...
    @staticmethod
    def from_u8(value: U8) -> Literal: ...
    @staticmethod
    def from_u16(value: U16) -> Literal: ...
    @staticmethod
    def from_u32(value: U32) -> Literal: ...
    @staticmethod
    def from_u64(value: U64) -> Literal: ...
    @staticmethod
    def from_u128(value: U128) -> Literal: ...
    def type_name(self) -> str: ...


class Locator:
    def __new__(cls, program_id: ProgramID, resource: Identifier) -> Locator: ...
    @staticmethod
    def from_string(s: str) -> Locator: ...
    def program_id(self) -> ProgramID: ...
    def name(self) -> Identifier: ...
    def network(self) -> Identifier: ...
    def resource(self) -> Identifier: ...


class Network:
    @staticmethod
    def name() -> str: ...
    @staticmethod
    def version() -> int: ...
    @staticmethod
    def edition() -> int: ...
    @staticmethod
    def hash_psd2(input: List[Field]) -> Field: ...


class MicroCredits:
    def __new__(cls, value: int) -> MicroCredits: ...
    def __int__(self) -> int: ...


class Plaintext:
    @staticmethod
    def from_string(s: str) -> Plaintext: ...
    @staticmethod
    def new_literal(literal: Literal) -> Plaintext: ...
    @staticmethod
    def new_struct(kv: List[Tuple[Identifier, Plaintext]]) -> Plaintext: ...
    @staticmethod
    def new_array(kv: List[Plaintext]) -> Plaintext: ...
    def encrypt(self, address: Address, randomizer: Scalar) -> Ciphertext: ...
    def encrypt_symmetric(self, plaintext_view_key: Field) -> Ciphertext: ...
    def is_literal(self) -> bool: ...
    def is_struct(self) -> bool: ...
    def is_array(self) -> bool: ...
    def as_literal(self) -> Literal: ...
    def as_struct(self) -> Mapping[Identifier, Plaintext]: ...
    def as_array(self) -> List[Plaintext]: ...


class PrivateKey:
    def address(self) -> Address: ...
    def compute_key(self) -> ComputeKey: ...
    @staticmethod
    def from_string(private_key: str) -> PrivateKey: ...
    @staticmethod
    def from_seed(seed: Field) -> PrivateKey: ...
    def seed(self) -> Field: ...
    def sign(self, message: bytes) -> Signature: ...
    def sk_sig(self) -> Scalar: ...
    def r_sig(self) -> Scalar: ...
    def view_key(self) -> ViewKey: ...


class Process:
    @staticmethod
    def load() -> Process: ...
    def add_program(self, program: Program) -> None: ...
    def contains_program(self, program_id: ProgramID) -> bool: ...

    def get_proving_key(self, program_id: ProgramID,
                        function_name: Identifier) -> ProvingKey: ...

    def insert_proving_key(self, program_id: ProgramID,
                           function_name: Identifier, proving_key: ProvingKey) -> None: ...

    def get_verifying_key(self, program_id: ProgramID,
                          function_name: Identifier) -> VerifyingKey: ...

    def insert_verifying_key(self, program_id: ProgramID,
                             function_name: Identifier, verifying_key: VerifyingKey) -> None: ...

    def authorize(self, private_key: PrivateKey, program_id: ProgramID,
                  function_name: Identifier, inputs: List[Value]) -> Authorization: ...

    def authorize_fee_private(self, private_key: PrivateKey, credits: RecordPlaintext, base_fee: MicroCredits,
                              deployment_or_execution_id: Field, priority_fee: Optional[MicroCredits]) -> Authorization: ...
    def authorize_fee_public(self, private_key: PrivateKey, base_fee: MicroCredits,
                             deployment_or_execution_id: Field, priority_fee: Optional[MicroCredits]) -> Authorization: ...

    def execute(self, authorization: Authorization) -> Tuple[Response, Trace]: ...
    def verify_execution(self, execution: Execution) -> None: ...
    def verify_fee(self, fee: Fee, deployment_or_execution_id: Field) -> None: ...
    def execution_cost(
        self, execution: Execution) -> Tuple[MicroCredits, Tuple[MicroCredits, MicroCredits]]: ...


class Program:
    @staticmethod
    def from_source(s: str) -> Program: ...
    @staticmethod
    def credits() -> Program: ...
    def id(self) -> ProgramID: ...
    def functions(self) -> List[Identifier]: ...
    def imports(self) -> List[ProgramID]: ...
    def source(self) -> str: ...


class ProgramID:
    @staticmethod
    def from_string(s: str) -> ProgramID: ...
    def name(self) -> Identifier: ...
    def network(self) -> Identifier: ...
    def is_aleo(self) -> bool: ...


class ProverSolution:
    def address(self) -> Address: ...
    def verify(self, verifying_key: CoinbaseVerifyingKey,
               epoch_challenge: EpochChallenge, proof_target: int) -> bool: ...

    @staticmethod
    def from_json(json: str) -> ProverSolution: ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_bytes(bytes: bytes) -> ProverSolution: ...
    def bytes(self) -> bytes: ...


class ProvingKey:
    @staticmethod
    def from_string(s: str) -> ProvingKey: ...
    @staticmethod
    def from_bytes(bytes: bytes) -> ProvingKey: ...
    def bytes(self) -> bytes: ...


class Query:
    @staticmethod
    def rest(url: str) -> Query: ...


class RecordCiphertext:
    @staticmethod
    def from_string(s: str) -> RecordCiphertext: ...
    def decrypt(self, view_key: ViewKey) -> RecordPlaintext: ...
    def is_owner(self, view_key: ViewKey) -> bool: ...


class RecordPlaintext:
    @staticmethod
    def from_string(s: str) -> RecordPlaintext: ...
    def owner(self) -> str: ...
    def nonce(self) -> Group: ...
    def serial_number(self, private_key: PrivateKey, program_id: ProgramID,
                      record_identifier: Identifier) -> Field: ...


class Response:
    def outputs(self) -> List[Value]: ...


class Scalar:
    @staticmethod
    def from_string(s: str) -> Scalar: ...
    @staticmethod
    def zero() -> Scalar: ...


class Signature:
    def challenge(self) -> Scalar: ...
    def compute_key(self) -> ComputeKey: ...
    @staticmethod
    def from_string(s: str) -> Signature: ...
    def response(self) -> Scalar: ...
    @staticmethod
    def sign(private_key: PrivateKey, message: bytes) -> Signature: ...
    def verify(self, address: Address, message: bytes) -> bool: ...


class Trace:
    def is_fee(self) -> bool: ...
    def is_fee_private(self) -> bool: ...
    def is_fee_public(self) -> bool: ...
    def transitions(self) -> List[Transition]: ...
    def prove_execution(self, locator: Locator) -> Execution: ...
    def prove_fee(self) -> Fee: ...
    def prepare(self, query: Query) -> None: ...


class Transaction:
    @staticmethod
    def from_execution(execution: Execution, fee: Optional[Fee]) -> Transaction: ...
    @staticmethod
    def from_json(json: str) -> Transaction: ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_bytes(bytes: bytes) -> Transaction: ...
    def bytes(self) -> bytes: ...


class Transition:
    def id(self) -> str: ...
    def program_id(self) -> ProgramID: ...
    def function_name(self) -> Identifier: ...
    def is_bond(self) -> bool: ...
    def is_unbond(self) -> bool: ...
    def is_fee_private(self) -> bool: ...
    def is_fee_public(self) -> bool: ...
    def is_split(self) -> bool: ...
    @staticmethod
    def from_json(json: str) -> Transition: ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_bytes(bytes: bytes) -> Transition: ...
    def bytes(self) -> bytes: ...


class U8:
    def __new__(cls, value: int) -> U8: ...
    @staticmethod
    def zero() -> U8: ...
    def __int__(self) -> int: ...


class U16:
    def __new__(cls, value: int) -> U16: ...
    @staticmethod
    def zero() -> U16: ...
    def __int__(self) -> int: ...


class U32:
    def __new__(cls, value: int) -> U32: ...
    @staticmethod
    def zero() -> U32: ...
    def __int__(self) -> int: ...


class U64:
    def __new__(cls, value: int) -> U64: ...
    @staticmethod
    def zero() -> U64: ...
    def __int__(self) -> int: ...


class U128:
    def __new__(cls, value: int) -> U128: ...
    @staticmethod
    def zero() -> U128: ...
    def __int__(self) -> int: ...


class Value:
    @staticmethod
    def parse(s: str) -> Value: ...
    @staticmethod
    def from_literal(literal: Literal) -> Value: ...
    @staticmethod
    def from_record_plaintext(record_plaintext: RecordPlaintext) -> Value: ...


class VerifyingKey:
    @staticmethod
    def from_string(s: str) -> VerifyingKey: ...
    @staticmethod
    def from_bytes(bytes: bytes) -> VerifyingKey: ...
    def bytes(self) -> bytes: ...


class ViewKey:
    def decrypt(self, record_ciphertext: RecordCiphertext) -> RecordPlaintext: ...
    @staticmethod
    def from_string(s: str) -> ViewKey: ...
    def is_owner(self, record_ciphertext: RecordCiphertext) -> bool: ...
    def to_address(self) -> Address: ...
