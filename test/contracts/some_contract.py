import tonos_ts4.ts4 as ts4


class Contract(ts4.BaseContract):
    def __init__(self, keypair=ts4.make_keypair(), balance=None):
        super().__init__(
            'Contract',
            ctor_params=dict(),
            keypair=keypair,
            balance=balance,
        )

    def add(self, v):
        return super().call_method(
            method='add',
            params=dict(v=v),
            private_key=self.private_key_,
        )
