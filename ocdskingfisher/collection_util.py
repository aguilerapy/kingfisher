import ocdskingfisher.database
import ocdskingfisher.sources_util
import os


class Collection:

    def __init__(self, source_id=None, data_version=None, sample=None, on_disk=None, database_id=None):
        self.source_id = source_id
        self.data_version = data_version
        self.sample = sample
        self.database_id = database_id
        self.on_disk = on_disk


def get_all_collections():
    out = []

    # Load from database
    with ocdskingfisher.database.get_engine().begin() as connection:
        s = ocdskingfisher.database.sa.sql.select([ ocdskingfisher.database.collection_table])
        for result in connection.execute(s):
            out.append(Collection(
                database_id=result['id'],
                source_id=result['source_id'],
                data_version=result['data_version'],
                sample=result['sample'],
            ))

    # Load from disk
    this_dir = os.path.dirname(os.path.realpath(__file__))
    base_dir = os.path.join(this_dir, "..", "data")

    for sample in [True, False]:
        for key in ocdskingfisher.sources_util.gather_sources().keys():
            directory = os.path.join(base_dir, key + ("_sample" if sample else ""))
            if os.path.isdir(directory):
                for version in os.listdir(directory):
                    if os.path.isdir(os.path.join(directory, version)) and \
                            os.path.isfile(os.path.join(directory, version, "metadb.sqlite3")):
                        _get_all_collections_disk_collection_found(
                            source_id=key,
                            data_version=version,
                            sample=sample,
                            out=out,
                        )

    # Return results
    return out


def _get_all_collections_disk_collection_found(source_id, data_version, sample, out):

    for existing in out:
        if existing.source_id == source_id and existing.data_version == data_version and existing.sample == sample:
            existing.on_disk = True
            return

    out.append(Collection(
        source_id=source_id,
        data_version=data_version,
        sample=sample,
        on_disk=True
    ))