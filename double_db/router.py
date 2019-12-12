class MainReplicaRouter:
    def db_for_read(self, model, **hints):
        """
        Reads go to a replica.
        """
        return 'read_replica'

    def db_for_write(self, model, **hints):
        """
        Writes always go to main.
        """
        return 'main'

    def allow_relation(self, obj1, obj2, **hints):
        """
        Relations between objects are allowed if both objects are
        in the main/read_replica pool.
        """
        db_list = ('main', 'read_replica')
        if obj1._state.db in db_list and obj2._state.db in db_list:
            return True
        return None

